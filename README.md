# ArticleAnalyzer_SBERT v9 (SBERT + NLP + Flask + Docker)

**Version:** 9.0
**Python:** 3.11
**Author:** Kyaw

---

## Project Overview

ArticleAnalyzer_SBERT is an **end-to-end news analysis system** that combines:

- NLP preprocessing (NER, summarization, keyword extraction)
- Sentence embeddings (SBERT) for semantic similarity
- KMeans clustering for grouping similar articles
- Sentiment analysis via pretrained transformer models
- Recommendations using FAISS indexing
- Web deployment with Flask and Docker

It demonstrates a complete ML/NLP lifecycle: **from raw data ingestion to production-ready API and web interface**.

---

## Features

### 1. End-to-End NLP Pipeline
- Load multiple CSV datasets and clean text
- Named Entity Recognition (NER) using BERT
- Summarization with distilBART CNN
- Frequency-based keyword extraction (top-k terms)
- Sentence embeddings via SBERT (`all-MiniLM-L6-v2`)
- KMeans clustering for article grouping
- Recommendations based on semantic similarity using FAISS

### 2. Sentiment Analysis
- Sentiment classification using `distilbert-base-uncased-finetuned-sst-2-english`
- Async prediction for fast batch processing
- Caching mechanism to avoid redundant computation

### 3. Deployment Ready
- Flask web interface:
  - List all articles
  - View detailed analysis (NER, summary, sentiment, keywords)
  - View article clusters and recommendations
- REST API:
  - `/api/analyze` – analyze single article
  - `/api/recommend` – fetch recommendations
  - `/api/clusters` – get cluster summaries
- Fully containerized with Docker & Docker Compose

### 4. Clean & Modular Code
- Clear separation of responsibilities:
  - `NLPEngine` – text preprocessing, NER, summarization, keywords
  - `EmbeddingEngine` – SBERT embeddings + FAISS recommendations
  - `SentimentAnalyzer` – async sentiment predictions
  - `Clusterer` – KMeans clustering
  - `NewsPipeline` – orchestrates the full pipeline
- Configurable via `data/config.json`
- Unit tests included for pipeline, embeddings, and API endpoints

---

## Folder Structure

```bash
v9/
├─ data/
│ ├─ business_news.csv
│ ├─ tech_news.csv
│ ├─ world_news.csv
│ └─ config.json
├─ models/ # Saved models (NER, summarizer, sentiment, embeddings)
├─ src/ # Core pipeline modules
│ ├─ __init__.py
│ ├─ nlp_engine.py
│ ├─ embedding_engine.py
│ ├─ sentiment_analyzer.py
│ ├─ clusterer.py
│ └─ news_pipeline.py
├─ app/ # Flask application
│ ├─ __init__.py
│ ├─ routes.py
│ ├─ templates/ # HTML templates for index, analysis, clusters
│ └─ static/ # CSS & JS assets
├─ tests/ # Unit tests
│ ├─ test_pipeline.py
│ ├─ test_embeddings.py
│ └─ test_api.py
├─ docker/
│ ├─ Dockerfile
│ └─ docker-compose.yml
├─ main.py # Pipeline runner & Flask entry
├─ requirements.txt
└─ README.md
```
---

## Setup

### 1. Local Python Environment
```bash
# Go to project folder
cd ~/ArticleAnalyzer_SBERT/v9

# Create & activate conda environment
conda create -n tf python=3.11 -y
conda activate tf

# Install dependencies
pip install -r requirements.txt

# Run the full pipeline (preprocessing, embeddings, clustering, sentiment, recommendations)
python main.py

# Launch Flask app
export FLASK_APP=app/routes.py
export FLASK_ENV=development  # optional for debug mode
flask run
```

### 2. Docker Deployment
```bash
# Build and run container
docker-compose build
docker-compose up

# Or individual commands
docker build -t articleanalyzer:v9 .
docker run -p 5000:5000 articleanalyzer:v9
```
## Testing
```bash
# Inside project folder with conda environment activated
python -m pytest -v tests
```
