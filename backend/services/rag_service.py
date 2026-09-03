"""
RAGService — semantic retrieval from ChromaDB.
Fix C-2: Uses per-domain collections (legal_consumer_law, legal_labour_law, etc.)
"""
from typing import Any

import chromadb
import structlog

from config import settings

log = structlog.get_logger()

_chroma_client: chromadb.AsyncHttpClient | None = None


async def _get_client() -> chromadb.AsyncHttpClient:
    global _chroma_client
    if _chroma_client is None:
        _chroma_client = await chromadb.AsyncHttpClient(
            host=settings.CHROMA_HOST,
            port=settings.CHROMA_PORT,
        )
    return _chroma_client


class RAGService:

    @staticmethod
    def _collection_name(legal_category: str) -> str:
        """
        Fix C-2: Build per-domain collection name.
        e.g. 'consumer_law' → 'legal_consumer_law'
        """
        safe = legal_category.lower().replace(" ", "_").replace("-", "_")
        return f"{settings.CHROMA_COLLECTION_PREFIX}{safe}"

    @classmethod
    async def retrieve(
        cls,
        query: str,
        legal_category: str,
        language: str = "si",
        top_k: int = 5,
    ) -> tuple[list[str], list[dict[str, Any]]]:
        """
        Retrieve top-k relevant legal chunks for the given query.
        Returns (context_texts, source_metadata).
        """
        try:
            client = await _get_client()
            collection_name = cls._collection_name(legal_category)

            try:
                collection = await client.get_collection(collection_name)
            except Exception:
                log.warning("Collection not found, returning empty context", collection=collection_name)
                return [], []

            results = await collection.query(
                query_texts=[query],
                n_results=top_k,
                where={"language": language} if language else None,
            )

            context_texts = results["documents"][0] if results["documents"] else []
            metadatas = results["metadatas"][0] if results["metadatas"] else []
            distances = results["distances"][0] if results["distances"] else []

            sources = []
            for meta, dist in zip(metadatas, distances):
                sources.append({
                    "source_id": meta.get("source_id"),
                    "chunk_id": meta.get("chunk_id"),
                    "title": meta.get("title", "Unknown"),
                    "section": meta.get("section"),
                    "url": meta.get("source_url"),
                    "relevance_score": round(1 - dist, 4),  # Convert distance to similarity
                })

            log.info("RAG retrieval complete", collection=collection_name, results=len(context_texts))
            return context_texts, sources

        except Exception as e:
            log.error("RAG retrieval failed", error=str(e))
            return [], []

    @classmethod
    async def index_chunk(
        cls,
        legal_category: str,
        chunk_id: str,
        source_id: str,
        text: str,
        metadata: dict[str, Any],
    ) -> None:
        """
        Add a legal chunk to the appropriate domain collection.
        Called by the indexer script when ingesting legal documents.
        """
        client = await _get_client()
        collection_name = cls._collection_name(legal_category)
        collection = await client.get_or_create_collection(collection_name)

        await collection.add(
            ids=[chunk_id],
            documents=[text],
            metadatas=[{**metadata, "source_id": source_id, "chunk_id": chunk_id}],
        )
        log.info("Chunk indexed", collection=collection_name, chunk_id=chunk_id)
