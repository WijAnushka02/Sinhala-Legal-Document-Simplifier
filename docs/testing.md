# 🧪 Testing Strategy

## Test Structure

```text
tests/
├── conftest.py              # Shared fixtures: async DB, mock services
├── unit/                    # Fast, isolated, no external I/O
│   ├── test_clause_classifier.py
│   ├── test_entity_extractor.py
│   ├── test_meaning_validator.py
│   └── test_rag_retriever.py
├── integration/             # Tests actual DB + API (uses in-memory SQLite test DB)
│   ├── test_simplification_api.py
│   ├── test_auth_api.py
│   └── test_document_api.py
└── e2e/                     # Full pipeline tests (may call real Gemini on staging)
    └── test_full_pipeline.py
```

## Running Tests

```bash
# All tests
pytest tests/ -v

# Unit only (fast, use in CI)
pytest tests/unit/ -v

# With coverage report
pytest tests/ --cov=backend --cov-report=html --cov-fail-under=70

# Integration tests (requires running DB)
pytest tests/integration/ -v

# Specific test file
pytest tests/unit/test_clause_classifier.py -v
```

## Coverage Targets

| Layer | Target |
|-------|--------|
| Legal processing (clause, entity, validation) | ≥ 80% |
| API endpoints | ≥ 75% |
| Services | ≥ 70% |
| RAG pipeline | ≥ 70% |
| **Overall** | **≥ 70%** |

## Key Test Cases

```python
# test_clause_classifier.py
def test_analyze_returns_legal_analysis(processor):
    text = "නියමිත කාල සීමාව තුළ අයදුම්පත ඉදිරිපත් කළ යුතුය."
    result = processor.analyze(text)
    assert isinstance(result, LegalAnalysis)

def test_analyze_single_pass_not_multiple_calls(processor):
    """Fix H-1: verify all outputs come from a single analyze() call."""
    text = "ගිවිසුමේ නියමයන් කඩ කළ විට රු. 50,000 ක දඩ මුදලකට යටත් වේ."
    result = processor.analyze(text)
    assert result.clause_types is not None
    assert result.entities is not None
    assert result.obligations is not None

# test_meaning_validator.py
def test_date_preserved(original_with_date, simplified_with_date):
    result = ValidationService._rule_based_validate(
        original_with_date, simplified_with_date, {}
    )
    assert result.dates_preserved is True
    assert result.meaning_score >= 0.85
```

## Test Fixtures (`conftest.py`)

- **`test_db`** — in-memory SQLite database, fresh for each test function
- **`client`** — `AsyncClient` with DB dependency overridden to use `test_db`
- **`sample_sinhala_legal_text`** — real Sinhala legal sentence for testing
- **`sample_simplified_text`** — expected simplified output

## CI Integration

Tests run automatically on every Pull Request via GitHub Actions:

```yaml
# .github/workflows/ci.yml
- pytest tests/unit/ --cov=backend --cov-fail-under=70
- mypy backend/
- ruff check backend/
```
