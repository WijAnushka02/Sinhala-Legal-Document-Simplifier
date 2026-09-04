# 📈 Scalability Design

## Architecture Scaling Strategy

```text
MVP (Single Server)
  └── All services on one VM / Docker Compose

Phase 2 (Horizontal Scaling)
  ├── Backend  → Multiple FastAPI replicas (Gunicorn workers or Cloud Run autoscaling)
  ├── Oracle → Connection pooling via PgBouncer
  ├── ChromaDB → Dedicated server or Weaviate Cloud
  └── Redis    → Upstash or ElastiCache

Phase 3 (High Load)
  ├── Message Queue (Redis Streams / Celery) for async simplification jobs
  ├── SLM inference → Dedicated GPU instance or TorchServe
  └── Document processing → Background worker pool
```

## Async Processing (Non-Blocking Pipeline)

The `/simplify` endpoint returns immediately — the AI pipeline runs in the background:

```text
Client ─── POST /simplify ──► FastAPI
                               │
                               ├── Returns: { session_id, status: "pending" }  ← immediate
                               │
                               └── BackgroundTasks.add_task(run_pipeline)
                                        │
                               SLM (thread pool) → RAG → Gemini → Validate
                                        │
                               Updates session in DB (status: "done")
                                        │
Client ─── GET /simplify/{session_id} ──► Returns completed result
```

**Phase 2**: Replace `BackgroundTasks` with Celery/ARQ for distributed workers.

## SLM Inference — Thread Pool

PyTorch inference is CPU/GPU-bound and blocks the event loop. All SLM calls run in a dedicated thread pool:

```python
_slm_executor = ThreadPoolExecutor(max_workers=2, thread_name_prefix="slm-worker")

result = await loop.run_in_executor(_slm_executor, slm_inference_fn, text)
```

## Caching Strategy

| Cache Target | TTL | Redis Key Pattern |
|---|---|---|
| RAG retrieval results (same query + category) | 1 hour | `rag:{category}:{query_hash}` |
| Gemini responses (deterministic prompts) | 30 min | `gemini:{prompt_hash}` |
| User profile data | 5 min | `user:{user_id}` |
| Legal source metadata | 24 hours | `legal_source:{source_id}` |

## Database Optimizations

- All foreign keys are indexed
- `simplification_sessions` indexed on `(user_id, created_at DESC)` for fast paginated history
- `legal_chunks` vector search happens in ChromaDB — not Oracle DB
- `asyncpg` driver for non-blocking Oracle DB I/O
- Connection pool: `pool_size=10, max_overflow=20`
- `pool_pre_ping=True` to detect stale connections

## ChromaDB Collection Segmentation

Legal chunks are split into per-domain collections to improve retrieval precision:

```text
legal_consumer_law      — Consumer Protection Act, etc.
legal_labour_law        — Shop and Office Employees Act, etc.
legal_property_law      — Land Registration Act, etc.
legal_family_law        — Marriage Registration Ordinance, etc.
legal_criminal_law      — Penal Code, etc.
legal_administrative_law — Administrative Tribunals Act, etc.
legal_general           — General legal provisions
```

Queries only search the relevant collection → faster retrieval, higher precision.
