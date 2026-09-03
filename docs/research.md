# ❗ Problem Statement

Sri Lankan legal documents often contain:

* Complex Sinhala terminology
* Long and formal sentences
* Legal terminology that is difficult for ordinary citizens to understand
* Multiple conditions and exceptions
* Complicated procedures
* Legal obligations and restrictions
* Important dates, deadlines, and numerical information

Although many legal documents are publicly available, **availability does not necessarily mean accessibility or understandability**.

For example, a citizen may have access to an Act, regulation, Gazette notification, or government legal document but may struggle to determine:

* What does this mean?
* What am I required to do?
* What are my rights?
* What documents are required?
* What is the deadline?
* What happens if I do not comply?
* Are there any exceptions?

Existing general-purpose AI systems can help explain such information, but they may introduce serious problems when dealing with legal content, including:

* Hallucination
* Missing important conditions
* Changing the original meaning
* Incorrect interpretation of legal terminology
* Incorrect dates or numbers
* Inventing information that does not exist in the source
* Providing confident answers without sufficient evidence

Therefore, there is a need for a system specifically designed to **simplify Sinhala legal information while preserving important legal meaning and grounding responses in verified sources**.

---

---

# 🎯 Project Objectives

### Primary Objective

Develop a Sinhala-focused Small Language Model capable of assisting with the understanding and simplification of Sri Lankan legal documents while preserving important legal information.

### Secondary Objectives

* Develop a curated Sinhala legal-language dataset.
* Train a lightweight Transformer-based language model.
* Develop a legal-document processing pipeline.
* Implement Retrieval-Augmented Generation using verified legal sources.
* Integrate Gemini API as a supporting AI component.
* Detect important legal entities and information.
* Validate simplified responses against the original legal content.
* Develop a web-based interface.
* Develop a telephone-based IVR/DTMF interface.
* Evaluate the system's accuracy, readability, and meaning preservation.

---

---

# 🧪 Research Experiments

The project can compare several approaches.

### Experiment 1

```text
SLM
```

### Experiment 2

```text
SLM + RAG
```

### Experiment 3

```text
Gemini + RAG
```

### Experiment 4

```text
SLM + Gemini
```

### Experiment 5

```text
SLM + RAG + Gemini + Validation
```

The performance of these approaches can then be compared.

This provides a strong research component for determining whether a **hybrid architecture can improve Sinhala legal-information accessibility and accuracy**.

---