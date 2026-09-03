"""ValidationService — meaning preservation scoring (stub + rule-based)."""
import re
from dataclasses import dataclass


@dataclass
class ValidationResult:
    meaning_score: float
    entity_preserved: bool
    dates_preserved: bool
    numbers_preserved: bool
    missing_elements: list[str]


class ValidationService:

    @classmethod
    async def validate(
        cls, original: str, simplified: str, analysis: dict
    ) -> dict:
        """
        Validate that the simplified text preserves the legal meaning of the original.
        Returns a dict compatible with SessionResult fields.
        """
        result = cls._rule_based_validate(original, simplified, analysis)
        return {
            "meaning_score": result.meaning_score,
            "entity_preserved": result.entity_preserved,
            "dates_preserved": result.dates_preserved,
            "numbers_preserved": result.numbers_preserved,
            "missing_elements": result.missing_elements,
        }

    @classmethod
    def _rule_based_validate(
        cls, original: str, simplified: str, analysis: dict
    ) -> ValidationResult:
        """
        Rule-based meaning preservation check.
        TODO: Enhance with semantic similarity model (SBERT) once embedding model is ready.
        """
        score = 1.0
        missing = []

        # Check entities are preserved
        entities = analysis.get("entities", [])
        entity_preserved = True
        for entity in entities:
            text = entity.get("text", "")
            if text and text not in simplified:
                entity_preserved = False
                score -= 0.1
                missing.append(f"Entity: {text}")

        # Check dates (simple number pattern check)
        date_pattern = re.compile(r'\b\d{1,4}[-/]\d{1,2}[-/]\d{1,4}\b|\bදින\s*\d+\b')
        original_dates = date_pattern.findall(original)
        dates_preserved = all(d in simplified for d in original_dates)
        if not dates_preserved:
            score -= 0.15
            missing.append("Date information may be missing")

        # Check numbers
        number_pattern = re.compile(r'\b\d{4,}\b|රු\.\s*[\d,]+')
        original_numbers = number_pattern.findall(original)
        numbers_preserved = all(n in simplified for n in original_numbers)
        if not numbers_preserved:
            score -= 0.15
            missing.append("Numerical values may be missing")

        # Length sanity check — simplified should be shorter but not too short
        if len(simplified) < len(original) * 0.1:
            score -= 0.2
            missing.append("Simplified text may be too short")

        return ValidationResult(
            meaning_score=max(0.0, min(1.0, score)),
            entity_preserved=entity_preserved,
            dates_preserved=dates_preserved,
            numbers_preserved=numbers_preserved,
            missing_elements=missing,
        )
