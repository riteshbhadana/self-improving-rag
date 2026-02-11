---
title: Self-Improving RAG System
emoji: 🧠
colorFrom: indigo
colorTo: purple
colorTo: purple
sdk: streamlit
sdk_version: 1.44.1
app_file: app.py
pinned: false
---

# 🧠 Self-Improving RAG System

A production-style Retrieval-Augmented Generation (RAG) system that evaluates its own answers, retries when confidence is low, and learns from human feedback.

This project demonstrates modern LLM architecture using:

- LangChain
- LangGraph
- Groq API (free inference)
- Streamlit UI
- Human feedback loop
- Self-evaluation pipeline

---

## 🚀 Features

✅ PDF document ingestion  
✅ Semantic retrieval (vector search)  
✅ LLM answer generation  
✅ Self-evaluation scoring  
✅ Automatic retry logic  
✅ Human feedback collection  
✅ Fault-tolerant API handling  
✅ Provider-agnostic LLM backend  
✅ Deployable Streamlit app  

---

## 🧠 Why “Self-Improving”?

Unlike normal RAG systems that just answer once and stop, this system:

1. Evaluates its own answer using an LLM judge
2. Retries if confidence is low
3. Stores human feedback (👍 / 👎)
4. Builds a dataset for continuous improvement

It doesn’t just answer — it learns from its mistakes.

---

## 🏗 Architecture

```
User Question
      ↓
Retriever (Vector DB)
      ↓
Generator LLM
      ↓
Evaluator LLM
      ↓
Retry if low score
      ↓
Store Feedback
```

This mirrors real-world AI production pipelines.

---

## 📂 Project Structure

```
self_improving_rag/
│
├── app.py                 # Streamlit UI
├── rag/
│   ├── loader.py          # PDF loader
│   ├── retriever.py       # Vector retrieval
│   └── generator.py       # Answer generation
│
├── evaluation/
│   └── evaluator.py       # Self-evaluation logic
│
├── graph/
│   └── rag_graph.py       # LangGraph workflow
│
├── memory/
│   ├── feedback_store.py  # Human feedback storage
│   └── feedback.json
│
└── requirements.txt
```

---

## ⚙ Installation

### 1. Clone repo

```
git clone <your_repo_url>
cd self_improving_rag
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 🔑 API Setup (Groq)

Create a free Groq account:

👉 https://console.groq.com

Create `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶ Run locally

```
python -m streamlit run app.py
```

Open browser → upload PDF → ask questions.

---

## ☁ Deploy on Hugging Face

1. Create Streamlit Space
2. Upload repo
3. Add secret:

```
GROQ_API_KEY
```

Your app is live 🎉

---

## 📊 Example Use Case

Upload a resume → ask:

> “What is his skill set?”

System retrieves skills section, extracts structured skills, evaluates answer quality, and logs feedback.

---

## 🎯 Skills Demonstrated

- Retrieval-Augmented Generation
- Prompt engineering
- Self-evaluation loops
- Human-in-the-loop AI
- Fault-tolerant API design
- LangGraph orchestration
- Vector search pipelines
- Production Streamlit deployment

---

## 🔮 Future Improvements

- Query rewriting
- Adaptive prompting
- Feedback analytics dashboard
- Structured JSON output
- Multi-document memory
- Active learning loop

---

## 🧑‍💻 Author

Built as an advanced LLM engineering project showcasing real-world RAG architecture.

---

## ⭐ If you like this project

Star the repo and share!

