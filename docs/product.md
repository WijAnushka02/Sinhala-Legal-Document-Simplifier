# 💡 Proposed Solution

The proposed system will provide an AI-powered platform for understanding Sinhala legal documents.

A user will be able to:

1. Select a preferred language.
2. Select a legal-information category.
3. Upload a legal document or enter legal text.
4. Ask questions about the document.
5. Retrieve relevant information from verified legal sources.
6. Receive a simplified Sinhala explanation.
7. View the original legal content alongside the simplified explanation.
8. Identify important conditions, obligations, dates, and entities.
9. Access legal information through a telephone-based IVR/DTMF interface.

The system will combine:

```text
Small Language Model
        +
Retrieval-Augmented Generation
        +
Gemini API
        +
Legal Meaning Validation
        +
Web / IVR Interface
```

---

---

# 🌐 Web Application

The web interface will provide a more detailed experience than the telephone interface.

### Main Features

* Language selection
* Legal category selection
* Legal document upload
* Text input
* Question answering
* Document simplification
* Key information extraction
* Source display
* Original vs simplified comparison
* Important condition highlighting
* Confidence / validation indicators

### Example Interface

```text
┌──────────────────────────────────────────────┐
│       🇱🇰 Sinhala Legal Document             │
│              Simplifier                     │
├──────────────────────────────────────────────┤
│                                              │
│ Language                                     │
│ [ සිංහල ] [ தமிழ் ] [ English ]             │
│                                              │
│ Legal Category                               │
│ [ Consumer Law ▼ ]                            │
│                                              │
│ Upload Document                              │
│ [ Upload PDF ]                               │
│                                              │
│ OR                                           │
│                                              │
│ Enter Legal Text                             │
│ ┌──────────────────────────────────────────┐ │
│ │                                          │ │
│ │ Paste legal text here...                 │ │
│ │                                          │ │
│ └──────────────────────────────────────────┘ │
│                                              │
│              [ Simplify ]                    │
└──────────────────────────────────────────────┘
```

### Result

```text
┌──────────────────────┬──────────────────────┐
│ Original Legal Text  │ Simplified Sinhala   │
├──────────────────────┼──────────────────────┤
│ Complex legal       │ Easy-to-understand   │
│ sentence...         │ explanation...       │
└──────────────────────┴──────────────────────┘

Important Information

✓ Obligation
✓ Deadline
✓ Condition
✓ Exception

Source:
Official Legal Document
```

---

---

# 🔒 Security

Security is especially important because the system may process user-provided legal documents.

### API Security

* Input validation
* Authentication
* Authorization
* Rate limiting
* CORS configuration
* Secure API endpoints

### Gemini API Security

The Gemini API key must be stored on the backend.

```text
Frontend
   │
   │ User Request
   ▼
FastAPI Backend
   │
   │ Gemini API Key
   ▼
Gemini API
```

The API key must **never** be included in:

* React source code
* GitHub repository
* Client-side JavaScript
* Public configuration files

Use environment variables:

```env
GEMINI_API_KEY=your_api_key
```

and add `.env` to `.gitignore`.

---

---

# ⚖️ Responsible AI & Legal Disclaimer

This system is intended to help users **understand publicly available legal information**.

It is not intended to:

* Replace lawyers
* Provide professional legal advice
* Make legal decisions
* Determine legal liability
* Predict court outcomes
* Replace official authorities

The system should clearly communicate uncertainty and provide references to the underlying legal sources whenever possible.

### User Disclaimer

> **මෙම පද්ධතිය නීතිමය උපදෙස් ලබා දීම සඳහා නොවේ. මෙහි ලබා දෙන සරල පැහැදිලි කිරීම් මුල් නීතිමය ලේඛන තේරුම් ගැනීමට සහාය වීම සඳහා පමණි. නීතිමය තීරණ ගැනීමට පෙර අදාළ නිල මූලාශ්‍ර හෝ සුදුසු නීතිමය වෘත්තිකයෙකුගෙන් උපදෙස් ලබා ගන්න.**

---
