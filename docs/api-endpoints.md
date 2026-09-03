# 🔌 API Endpoints

**Base URL**: `http://localhost:8000/api/v1`

**Authentication**: Include `Authorization: Bearer <jwt_token>` header for protected routes, or `X-API-Key: <api_key>` for programmatic access.

**Swagger UI** (development only): `http://localhost:8000/docs`

---

## 🔑 Authentication

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `POST` | `/auth/register` | Public | Create a new user account |
| `POST` | `/auth/login` | Public | Obtain JWT access + refresh tokens |
| `POST` | `/auth/refresh` | Refresh cookie | Rotate to new access token |
| `POST` | `/auth/logout` | JWT | Invalidate refresh token |
| `GET`  | `/auth/me` | JWT | Get current user profile |

### `POST /auth/register`

```json
// Request
{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "display_name": "Anushka"
}

// Response 201
{
  "id": "uuid",
  "email": "user@example.com",
  "display_name": "Anushka",
  "created_at": "2026-09-03T12:00:00Z"
}
```

### `POST /auth/login`

```json
// Request
{
  "email": "user@example.com",
  "password": "SecurePass123!"
}

// Response 200
// Refresh token is set as HttpOnly cookie automatically
{
  "access_token": "eyJ...",
  "token_type": "bearer",
  "expires_in": 900
}
```

---

## 📄 Documents

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `POST` | `/documents/upload` | JWT | Upload a PDF or DOCX legal document |
| `GET`  | `/documents` | JWT | List user's uploaded documents |
| `GET`  | `/documents/{id}` | JWT | Get document metadata |
| `DELETE` | `/documents/{id}` | JWT | Delete a document |

### `POST /documents/upload`

```
Content-Type: multipart/form-data

Fields:
  file           - PDF or DOCX file (max 10 MB)
  language       - "si" | "ta" | "en"  (default: "si")
  legal_category - string (optional)

Response 202
{
  "id": "uuid",
  "filename": "consumer_act.pdf",
  "status": "processing",
  "created_at": "2026-09-03T12:00:00Z"
}
```

---

## ✨ Simplification _(Core Endpoint)_

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `POST` | `/simplify` | JWT or API Key | Submit text or document for simplification |
| `GET`  | `/simplify/{session_id}` | JWT or API Key | Poll / fetch completed result |

The endpoint returns immediately with `status: "pending"`. Poll `GET /simplify/{session_id}` until `status` is `"done"` or `"error"`.

### `POST /simplify`

```json
// Request — Text Input
{
  "input_type": "text",
  "text": "නියමිත කාල සීමාව තුළ අයදුම්පත ඉදිරිපත් කිරීමට...",
  "language": "si",
  "legal_category": "consumer_law",
  "use_rag": true,
  "use_gemini": true
}

// Request — Document Input
{
  "input_type": "document",
  "document_id": "uuid",
  "language": "si",
  "legal_category": "consumer_law",
  "use_rag": true,
  "use_gemini": true
}

// Response 202 (immediate)
{
  "session_id": "uuid",
  "status": "pending",
  "created_at": "2026-09-03T12:00:00Z"
}

// GET /simplify/{session_id} — Response when done
{
  "session_id": "uuid",
  "status": "done",
  "original_text": "නියමිත කාල සීමාව...",
  "simplified_text": "අයදුම්පත නියමිත කාලය ඇතුළත ලබා දිය යුතුය...",
  "clause_types": ["OBLIGATION", "DEADLINE"],
  "entities": [
    { "text": "අයදුම්කරු", "type": "PERSON_ROLE" }
  ],
  "conditions": ["Application not submitted in time"],
  "obligations": ["Applicant must reapply"],
  "exceptions": [],
  "meaning_score": 0.94,
  "sources": [
    {
      "source_id": "uuid",
      "title": "Consumer Protection Act No. 09 of 2003",
      "section": "Section 12",
      "relevance_score": 0.87,
      "url": "https://..."
    }
  ],
  "processing_time_ms": 2340,
  "slm_used": true,
  "rag_used": true,
  "gemini_used": true
}
```

---

## ❓ Question Answering (RAG Query)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `POST` | `/query` | JWT or API Key | Ask a legal question grounded in RAG |

### `POST /query`

```json
// Request
{
  "question": "ජාවාරම් නීතිය යටතේ පාරිභෝගිකයෙකුගේ අයිතිවාසිකම් මොනවාද?",
  "language": "si",
  "legal_category": "consumer_law",
  "session_id": "uuid"   // optional — provide document context
}

// Response 200
{
  "session_id": "uuid",
  "answer": "ජාවාරම් නීතිය යටතේ...",
  "sources": [...],
  "confidence": 0.89,
  "processing_time_ms": 1890
}
```

---

## 📜 History

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `GET`  | `/history` | JWT | List user's previous sessions (paginated) |
| `GET`  | `/history/{session_id}` | JWT | Get full session detail |
| `DELETE` | `/history/{session_id}` | JWT | Delete session record |

### `GET /history`

```
Query params:
  page      (default: 1)
  limit     (default: 20, max: 100)
  category  (optional filter)

Response 200
{
  "items": [
    {
      "session_id": "uuid",
      "status": "done",
      "legal_category": "consumer_law",
      "meaning_score": 0.94,
      "created_at": "2026-09-03T12:00:00Z"
    }
  ],
  "page": 1,
  "limit": 20
}
```

---

## 🔑 API Keys (Developer Access)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `POST`   | `/api-keys` | JWT | Create a new API key |
| `GET`    | `/api-keys` | JWT | List user's API keys |
| `DELETE` | `/api-keys/{id}` | JWT | Revoke an API key |

> The raw key is shown **only once** on creation. Store it securely.

---

## 🩺 Health

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `GET` | `/health` | Public | Liveness check |
| `GET` | `/health/ready` | Public | Readiness check (DB + ChromaDB + Redis) |

```json
// GET /health/ready — Response 200
{
  "status": "ready",
  "checks": {
    "database": "ok",
    "redis": "ok",
    "vector_store": "ok"
  },
  "version": "1.0.0"
}
```

---

## Error Responses

All errors follow this format:

```json
{
  "detail": "Human-readable error message"
}
```

| Status | Meaning |
|---|---|
| `400` | Bad request / validation error |
| `401` | Unauthenticated |
| `403` | Forbidden |
| `404` | Not found |
| `409` | Conflict (e.g. email already registered) |
| `413` | File too large |
| `415` | Unsupported media type |
| `422` | Unprocessable entity (Pydantic validation) |
| `429` | Rate limit exceeded |
| `500` | Internal server error |
