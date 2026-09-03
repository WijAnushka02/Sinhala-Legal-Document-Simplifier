# SLM↔Gemini Routing Architecture Decision Record

## Context

The system uses three AI components:

| Component | Role | Cost |
|---|---|---|
| **SLM** (Small Language Model) | Sinhala-specialized extraction + simplification | Zero (local) |
| **RAG** (ChromaDB retrieval) | Ground responses in verified legal sources | Zero (local) |
| **Gemini API** | High-quality reasoning and generation | Per-call (paid) |

## Decision Tree (Fix H-3)

```
Input received
     │
[Step 1] SLM multi-task analysis (always runs)
     │
     ├─ Outputs: clause_types, entities, obligations, conditions,
     │           simplified_text, confidence (0.0–1.0)
     │
[Step 2] Is SLM confidence ≥ 0.75 AND user did not request Gemini?
     │
     ├── YES ──► Use SLM simplified_text directly
     │           └── Skip Gemini (cost saving)
     │
     └── NO ───► [Step 3] RAG retrieval (if legal_category provided)
                     │
                 [Step 4] Call Gemini with:
                     - Original text
                     - SLM analysis (as context)
                     - RAG chunks (as grounding)
                     │
                 Gemini unavailable? (timeout/quota/error)
                     │
                     ├── Fallback: use SLM result
                     │   Set error_code = "GEMINI_FALLBACK"
                     │   Return result with warning
                     │
                     └── Continue with Gemini result
```

## Error Codes

| Code | Meaning |
|---|---|
| `GEMINI_TIMEOUT` | Gemini API did not respond within 30s |
| `GEMINI_RATE_LIMIT` | Gemini API quota exceeded |
| `GEMINI_CONTENT_FILTERED` | Gemini refused to process content |
| `GEMINI_FALLBACK` | Gemini failed; SLM result used instead |
| `SLM_INFERENCE_ERROR` | SLM forward pass failed |
| `OCR_FAILURE` | Could not extract text from image PDF |
| `PDF_CORRUPT` | PDF file could not be read |
| `RAG_NO_RESULTS` | No relevant chunks found in vector store |
| `VALIDATION_FAILED` | Meaning score below minimum threshold |
| `INTERNAL_ERROR` | Unexpected server error |

## Per-Task Temperature Configuration (Fix M-4)

| Task | Temperature | Rationale |
|---|---|---|
| `simplification` | 0.1 | Factual, minimal creativity — preserve legal meaning |
| `validation` | 0.0 | Deterministic comparison |
| `query_answer` | 0.1 | Factual answer from context |
| `reformulation` | 0.4 | Some creativity for query rewriting |
| `dataset_generation` | 0.7 | Diversity needed for training data |

## ChromaDB Collection Strategy (Fix C-2)

Collections are segmented by legal domain:

```
legal_consumer_law
legal_labour_law
legal_property_law
legal_family_law
legal_criminal_law
legal_administrative_law
legal_general
```

Collection name = `{CHROMA_COLLECTION_PREFIX}{legal_category}`
Default prefix: `legal_`
