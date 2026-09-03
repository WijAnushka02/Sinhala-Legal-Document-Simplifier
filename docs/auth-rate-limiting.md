# 🔐 Authentication & Rate Limiting

## JWT Flow

```text
1. User POSTs credentials to /auth/login
2. Backend verifies password hash (bcrypt, cost factor 12)
3. Backend issues:
     access_token  — short-lived (15 min), returned in JSON body
     refresh_token — long-lived (30 days), set as HttpOnly cookie
4. Client stores access_token in memory (NOT localStorage — XSS risk)
5. Client sends: Authorization: Bearer <access_token> on each request
6. At expiry, client POSTs to /auth/refresh (browser sends HttpOnly cookie automatically)
7. Backend rotates refresh token and issues new access token
```

## API Key Flow (Developer / Programmatic Access)

```text
1. Authenticated user calls POST /api-keys → receives raw key ONCE (shown only once)
2. Backend stores SHA-256(raw_key) in api_keys table — never the raw key
3. Developer includes X-API-Key: <raw_key> on requests
4. Backend hashes incoming key and looks up the hash
```

## Rate Limiting Strategy

Rate limiting uses **Redis sliding window** (not PostgreSQL) for correctness and performance under concurrent load.

```text
Endpoint                   Limit
─────────────────────────────────────────────────────────
POST /simplify             10 requests / minute / user
POST /query                20 requests / minute / user
POST /documents/upload      5 requests / minute / user
All others                100 requests / minute / user
```

Exceeded limits return:

```json
HTTP 429 Too Many Requests
{
  "detail": "Rate limit exceeded. Try again in 60 seconds.",
  "retry_after": 60
}
```

## Security Checklist

- [x] Passwords hashed with **bcrypt** (cost factor 12)
- [x] API keys stored as **SHA-256 hashes** only — raw key shown once
- [x] JWT signed with **HS256** using a strong secret
- [x] Refresh token stored in **HttpOnly cookie** — not accessible to JavaScript
- [x] Access token stored **in-memory** on client — not in localStorage
- [x] **CORS** restricted to known origins via `ALLOWED_ORIGINS` env var
- [x] **Input validation** via Pydantic v2 on all request bodies
- [x] **File type validation** — MIME type check + size limit enforced
- [x] **SQL injection** prevented via SQLAlchemy ORM (parameterized queries)
- [x] **Gemini API key** never exposed to frontend — backend only
- [x] **`.env` in `.gitignore`** — never committed
- [x] Dependency **security scanning** via `pip-audit` in CI
- [x] **HTTPS** enforced in production (Nginx / cloud provider TLS)
- [x] Rate limiting backed by **Redis** — no PostgreSQL bottleneck
