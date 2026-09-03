"""
Unit tests for the LegalProcessor (clause classifier + entity extractor).
These tests run against the stub — replace with real model assertions once trained.
"""
import pytest
from legal.legal_processor import LegalProcessor, LegalAnalysis


@pytest.fixture
def processor():
    return LegalProcessor()


def test_analyze_returns_legal_analysis(processor):
    """analyze() should return a LegalAnalysis dataclass."""
    text = "නියමිත කාල සීමාව තුළ අයදුම්පත ඉදිරිපත් කළ යුතුය."
    result = processor.analyze(text)
    assert isinstance(result, LegalAnalysis)


def test_analyze_has_all_fields(processor):
    """All expected fields should be present in the result."""
    text = "සේවාලාභියා රැකියාවෙන් ඉවත් කළ හොත් දින 30ක් කල්තියා දැනුම් දිය යුතුය."
    result = processor.analyze(text)
    assert hasattr(result, 'clause_types')
    assert hasattr(result, 'entities')
    assert hasattr(result, 'obligations')
    assert hasattr(result, 'conditions')
    assert hasattr(result, 'exceptions')
    assert hasattr(result, 'confidence')
    assert isinstance(result.confidence, float)
    assert 0.0 <= result.confidence <= 1.0


def test_analyze_does_not_raise_on_empty_input(processor):
    """Should handle edge-case empty input without crashing."""
    result = processor.analyze("")
    assert isinstance(result, LegalAnalysis)


def test_analyze_single_pass_not_multiple_calls(processor):
    """
    Verify that a single analyze() call is sufficient.
    The processor must NOT require separate calls for clause/entity/obligation.
    This test documents the design constraint from H-1 fix.
    """
    text = "ගිවිසුමේ නියමයන් කඩ කළ විට රු. 50,000 ක දඩ මුදලකට යටත් වේ."
    result = processor.analyze(text)
    # All results come from ONE call — this is the contract
    assert result.clause_types is not None
    assert result.entities is not None
    assert result.obligations is not None
