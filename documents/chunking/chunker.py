"""
Clause-boundary-aware chunker for Sinhala legal text.
Fix M-5: Implements documented chunking strategy.
"""
import re
from dataclasses import dataclass


@dataclass
class TextChunk:
    text: str
    chunk_index: int
    source_section: str | None = None
    token_count: int = 0


class LegalTextChunker:
    """
    Chunking strategy for Sri Lankan legal documents.

    Rules (fix M-5):
    1. Primary split: at section headings (§, numbered provisions like "1.", "2(a)")
    2. Secondary split: at sentence boundaries
    3. Minimum chunk size: 50 tokens (merge short clauses)
    4. Maximum chunk size: 256 tokens
    5. Overlap: 20 tokens to preserve clause transitions
    6. Always include: section number in chunk metadata
    """

    MIN_TOKENS = 50
    MAX_TOKENS = 256
    OVERLAP_TOKENS = 20

    # Sinhala section patterns + English legal numbering
    SECTION_PATTERN = re.compile(
        r"(?:^|\n)(?:§\s*\d+|^\d+\.\s|\(\w+\)\s|වගන්ති\s*\d+|ඡේදය\s*\d+)",
        re.MULTILINE,
    )

    def chunk(self, text: str) -> list[TextChunk]:
        """Split legal text into clause-boundary-aware chunks."""
        # Primary split on section headings
        sections = self.SECTION_PATTERN.split(text)
        section_headers = self.SECTION_PATTERN.findall(text)

        chunks: list[TextChunk] = []
        chunk_idx = 0

        for i, section in enumerate(sections):
            header = section_headers[i].strip() if i < len(section_headers) else None
            sentences = self._split_sentences(section)

            current_chunk_tokens: list[str] = []
            current_text_parts: list[str] = []

            for sentence in sentences:
                tokens = sentence.split()  # Approximate tokenization
                if len(current_chunk_tokens) + len(tokens) > self.MAX_TOKENS:
                    # Flush current chunk
                    if len(current_chunk_tokens) >= self.MIN_TOKENS:
                        chunks.append(TextChunk(
                            text=" ".join(current_text_parts),
                            chunk_index=chunk_idx,
                            source_section=header,
                            token_count=len(current_chunk_tokens),
                        ))
                        chunk_idx += 1
                        # Keep overlap
                        overlap = current_chunk_tokens[-self.OVERLAP_TOKENS:]
                        current_chunk_tokens = overlap
                        current_text_parts = [" ".join(overlap)]
                    else:
                        current_chunk_tokens.extend(tokens)
                        current_text_parts.append(sentence)
                else:
                    current_chunk_tokens.extend(tokens)
                    current_text_parts.append(sentence)

            # Flush remaining
            if current_chunk_tokens and len(current_chunk_tokens) >= self.MIN_TOKENS:
                chunks.append(TextChunk(
                    text=" ".join(current_text_parts),
                    chunk_index=chunk_idx,
                    source_section=header,
                    token_count=len(current_chunk_tokens),
                ))
                chunk_idx += 1

        return chunks

    def _split_sentences(self, text: str) -> list[str]:
        """Split on Sinhala sentence endings (。|. followed by capital or Sinhala char)."""
        parts = re.split(r"(?<=[.!?।])\s+", text.strip())
        return [p.strip() for p in parts if p.strip()]
