# 📚 Legal Dataset

The dataset will contain carefully collected and processed Sinhala legal information.

Potential sources include:

* Sri Lankan Acts
* Regulations
* Gazette notifications
* Legal notices
* Government legal documents
* Public legal information
* Official government publications
* Publicly available legal documents

Official sources should be prioritized wherever possible.

### Dataset Example

```json
{
  "language": "si",
  "category": "consumer_law",
  "clause_type": "OBLIGATION",
  "legal_text": "නියමිත කාලසීමාව තුළ අයදුම්පත ඉදිරිපත් කළ යුතුය.",
  "simplified_text": "අයදුම්පත නියමිත කාලය ඇතුළත ලබා දිය යුතුය.",
  "entities": [],
  "conditions": [],
  "exceptions": [],
  "source": "Official Legal Source"
}
```

### Dataset Fields

```text
Document ID
Original Text
Simplified Text
Language
Legal Category
Clause Type
Entities
Dates
Numbers
Conditions
Exceptions
Obligations
Source
Publication Date
Last Verified Date
```

---

---

# 📊 Evaluation Metrics

The system will be evaluated using multiple dimensions.

## SLM Evaluation

* Accuracy
* Precision
* Recall
* F1 Score
* Perplexity
* Intent Classification Accuracy

## RAG Evaluation

* Retrieval Accuracy
* Context Relevance
* Answer Faithfulness
* Source Accuracy
* Hallucination Rate

## Simplification Evaluation

* Semantic Similarity
* Readability
* Fluency
* Meaning Preservation
* Human Evaluation

## Legal Information Preservation

The system will specifically evaluate:

```text
Entity Preservation
Date Preservation
Number Preservation
Condition Preservation
Obligation Preservation
Exception Preservation
Requirement Preservation
Procedure Preservation
Penalty Preservation
```

---
