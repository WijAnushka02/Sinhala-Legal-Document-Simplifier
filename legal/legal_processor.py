"""
LegalProcessor — orchestrates a SINGLE SLM forward pass returning all analysis.
Fix H-1: One multi-task inference call instead of 4 separate module calls.
"""
from dataclasses import dataclass, field
from typing import Any


@dataclass
class LegalAnalysis:
    """Result of the unified legal text analysis pass."""
    clause_types: list[str] = field(default_factory=list)
    entities: list[dict[str, str]] = field(default_factory=list)
    obligations: list[str] = field(default_factory=list)
    conditions: list[str] = field(default_factory=list)
    exceptions: list[str] = field(default_factory=list)
    dates: list[dict[str, Any]] = field(default_factory=list)
    numbers: list[dict[str, Any]] = field(default_factory=list)
    simplified_text: str = ""
    confidence: float = 0.0


class LegalProcessor:
    """
    Unified legal text analysis using a single SLM multi-task forward pass.

    TODO: Replace stub with actual trained SLM once model/inference.py is ready.
    The SLM should output all fields in a single structured prediction to avoid
    running multiple separate forward passes on the same input (H-1 fix).
    """

    def __init__(self, model_path: str | None = None):
        self.model_path = model_path
        self._model = None  # Lazy-loaded when first needed

    def _load_model(self):
        """Lazy-load the SLM. Replace with actual model loading."""
        # from model.inference import SLMInference
        # self._model = SLMInference(self.model_path)
        self._model = "stub"

    def analyze(self, text: str) -> LegalAnalysis:
        """
        Single forward pass — returns all analysis dimensions at once.
        Runs synchronously; call via asyncio.run_in_executor from async code.
        """
        if self._model is None:
            self._load_model()

        # ── TODO: Replace with actual SLM inference ──────────────────────────
        # result = self._model.analyze_all(text)
        # return LegalAnalysis(**result)

        # Stub: returns placeholder analysis
        return LegalAnalysis(
            clause_types=["OBLIGATION"],
            entities=[{"text": "ලේඛනය", "type": "DOCUMENT"}],
            obligations=["Submit within the specified time period"],
            conditions=[],
            exceptions=[],
            dates=[],
            numbers=[],
            simplified_text=text,
            confidence=0.5,
        )


# Module-level singleton
legal_processor = LegalProcessor()
