"""
Unit tests for ValidationService.
"""
import pytest
import asyncio
from backend.services.validation_service import ValidationService


@pytest.fixture
def original_with_date():
    return "නියමිත දින 30 ඇතුළත අයදුම්කරු විසින් අයදුම්පත ඉදිරිපත් කළ යුතුය."


@pytest.fixture
def simplified_with_date():
    return "දින 30 ඇතුළත අයදුම්පත ලබා දිය යුතුය."


@pytest.fixture
def simplified_missing_date():
    return "අයදුම්පත ලබා දිය යුතුය."


def test_date_preserved(original_with_date, simplified_with_date):
    result = ValidationService._rule_based_validate(
        original_with_date, simplified_with_date, {}
    )
    assert result.dates_preserved is True
    assert result.meaning_score >= 0.85


def test_date_missing_lowers_score(original_with_date, simplified_missing_date):
    result = ValidationService._rule_based_validate(
        original_with_date, simplified_missing_date, {}
    )
    assert result.dates_preserved is False
    assert result.meaning_score < 1.0


def test_entity_missing_lowers_score():
    original = "නියමිත කාල සීමාව ඇතුළත ලබා නොදුන් විට..."
    simplified = "කාලය ගිය විට..."
    analysis = {"entities": [{"text": "නියමිත කාල සීමාව", "type": "DEADLINE"}]}
    result = ValidationService._rule_based_validate(original, simplified, analysis)
    assert result.entity_preserved is False
    assert result.meaning_score < 0.95
