"""
GeminiService — wrapper around the google-genai SDK.
Fix M-4: Per-task temperature configuration (not a single global value).
Fix H-3: Explicit task routing with fallback handling.
"""
import structlog
from google import genai
from google.genai import types

from config import settings

log = structlog.get_logger()

# Fix M-4: Per-task temperatures — not a single env var
TASK_CONFIG = {
    "simplification": types.GenerateContentConfig(temperature=0.1, max_output_tokens=4096),
    "validation":     types.GenerateContentConfig(temperature=0.0, max_output_tokens=1024),
    "query_answer":   types.GenerateContentConfig(temperature=0.1, max_output_tokens=2048),
    "reformulation":  types.GenerateContentConfig(temperature=0.4, max_output_tokens=512),
    "dataset_gen":    types.GenerateContentConfig(temperature=0.7, max_output_tokens=4096),
}

_client: genai.Client | None = None


def _get_client() -> genai.Client:
    global _client
    if _client is None:
        _client = genai.Client(api_key=settings.GEMINI_API_KEY)
    return _client


class GeminiService:

    @classmethod
    async def simplify(
        cls,
        original_text: str,
        rag_context: list[str],
        language: str = "si",
        legal_category: str | None = None,
    ) -> str:
        """Simplify legal text using Gemini with RAG context."""
        context_block = "\n\n".join(rag_context) if rag_context else "No additional context available."

        lang_name = {"si": "Sinhala (සිංහල)", "ta": "Tamil (தமிழ்)", "en": "English"}.get(language, "Sinhala")

        prompt = f"""You are a legal document simplification assistant specializing in Sri Lankan law.

TASK: Simplify the following legal text into plain {lang_name} that an ordinary citizen can understand.

STRICT RULES:
1. Do NOT change the legal meaning, obligations, rights, conditions, or consequences.
2. Do NOT add information that is not in the original text.
3. Do NOT remove important legal obligations, deadlines, or conditions.
4. If uncertain about the meaning, preserve the original wording.

VERIFIED LEGAL CONTEXT (from official sources):
{context_block}

ORIGINAL LEGAL TEXT:
{original_text}

SIMPLIFIED TEXT (in {lang_name}):"""

        client = _get_client()
        response = await client.aio.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=prompt,
            config=TASK_CONFIG["simplification"],
        )
        return response.text.strip()

    @classmethod
    async def answer_query(
        cls,
        question: str,
        rag_context: list[str],
        language: str = "si",
    ) -> str:
        """Answer a legal question using RAG context."""
        context_block = "\n\n".join(rag_context) if rag_context else "No context available."

        prompt = f"""You are a legal information assistant for Sri Lanka.
Answer the following question ONLY based on the provided legal context.
If the answer is not in the context, say "This information is not available in the current legal sources."

LEGAL CONTEXT:
{context_block}

QUESTION: {question}

ANSWER (in the same language as the question):"""

        client = _get_client()
        response = await client.aio.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=prompt,
            config=TASK_CONFIG["query_answer"],
        )
        return response.text.strip()

    @classmethod
    async def validate_meaning(cls, original: str, simplified: str) -> dict:
        """Use Gemini to compare original and simplified for meaning preservation."""
        prompt = f"""Compare these two legal texts and check if important legal information is preserved.

ORIGINAL: {original}
SIMPLIFIED: {simplified}

Return a JSON object with:
- preserved: true/false
- missing_elements: list of important elements missing from simplified
- score: 0.0-1.0 meaning preservation score"""

        client = _get_client()
        response = await client.aio.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=prompt,
            config=TASK_CONFIG["validation"],
        )
        return {"raw": response.text}
