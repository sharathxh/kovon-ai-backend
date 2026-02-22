# 🚀 Kovon AI Backend Hiring Assignment  
## Semantic Candidate–Job Matching Engine

---

## 📌 Objective

This project implements a Python backend service that performs semantic matching between candidate profiles and job descriptions using vector embeddings and FAISS similarity search.

The system:
- Stores candidate profiles
- Stores job descriptions
- Generates embeddings
- Performs cosine similarity matching
- Returns ranked candidate matches

---

## 🛠️ Tech Stack

- Python 3.10+
- FastAPI
- FAISS (Vector Database)
- HuggingFace Sentence Transformers
- Pydantic

---

## 📂 Project Structure

```
app/
 ├── main.py
 ├── api/
 │     ├── candidate_routes.py
 │     ├── job_routes.py
 ├── services/
 │     ├── embedding_service.py
 │     ├── matching_service.py
 ├── db/
 │     ├── faiss_store.py
 ├── models/
 │     ├── candidate_model.py
 │     ├── job_model.py
 ├── schemas/
 │     ├── candidate_schema.py
 │     ├── job_schema.py
 └── config.py
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd kovon_ai_backend
```

### 2️⃣ Create Virtual Environment

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Server

```bash
venv\Scripts\python -m uvicorn app.main:app
```

Open Swagger UI:
```
http://127.0.0.1:8000/docs
```

---

## 🧠 Embedding Model Used

Model: `all-MiniLM-L6-v2`  
Source: HuggingFace Sentence Transformers

- Generates 384-dimensional dense embeddings
- Optimized for semantic similarity tasks
- Lightweight and CPU-efficient

All candidate skill descriptions and job descriptions are converted into vector embeddings before similarity comparison.

---

## 🔍 Similarity Metric Explanation

Cosine similarity is used to measure semantic similarity between job descriptions and candidate skill descriptions.

Formula:

cos(A, B) = (A · B) / (||A|| ||B||)

Implementation details:

- All vectors are L2-normalized before indexing.
- FAISS `IndexFlatIP` is used for similarity search.
- Since vectors are normalized, inner product equals cosine similarity.
- Results are ranked by:
  1. Higher similarity score
  2. Higher experience (tie-breaker)

---

## 📦 API Endpoints

### Create Candidate
POST `/candidates`

Example:
```json
{
  "name": "Rahul",
  "skill_description": "Registered nurse with 4 years ICU experience and German A2 level",
  "experience": 4,
  "location": "India"
}
```

---

### Create Job
POST `/jobs`

Example:
```json
{
  "title": "ICU Nurse",
  "country": "Germany",
  "description": "Looking for ICU nurse with hospital experience and basic German"
}
```

---

### Match Candidates to Job
GET `/jobs/{job_id}/match`

Returns top 5 ranked candidates based on:
- Semantic similarity score
- Experience (tie-breaker)

---

## 📝 Notes

- Candidate embeddings are stored in FAISS.
- Job embeddings are generated during matching.
- Data is stored in memory for demonstration purposes.
- FAISS index resets when server restarts.
