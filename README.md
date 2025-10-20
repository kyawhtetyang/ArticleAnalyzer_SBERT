## Fake News Classification LSTM — Version History v1–v10

An evolving NLP project for news article analysis, developed across 9 structured versions — from basic preprocessing and sentiment analysis to a full multi-task system with recommendations, clustering, and web deployment.

### Project Versions and Evolution
* [v1](./v1) — Basic CSV loader, and sentiment analysis
* [v2](./v2) — Added NER and summarization (Hugging Face pipelines)
* [v3](./v3) — Multi-task NLP: sentiment, NER, summarization, keywords
* [v4](./v4) — Cleaner code structure
* [v5](./v5) — TF-IDF + SQLite recommendation  
* [v6](./v6) — SBERT + SQLite recommendation
* [v7](./v7) — Pipeline-structured Recommendation with API
* [v8](./v8) — Object-Oriented Recommendation
* [v9](./v9) — Production-ready Recommendation, Flask, Docker, testing

Features
NLP pipeline: preprocessing, NER, summarization, keyword extraction
SBERT embeddings + FAISS recommendations + KMeans clustering
Async sentiment analysis with caching
Flask web app + REST API endpoints
Modular, configurable, tested, Docker-ready

### Folder Structure (Simplified)
```php
ArticleAnalyzer_SBERT/
├─ v1   # CSV + Sentiment + Flask
├─ v2   # NER + Summarization
├─ v3   # Sentiment + NER + Summary + Keywords
├─ v4   # Cleaner code structure
├─ v5   # TF-IDF + SQLite recommendation
├─ v6   # SBERT + SQLite recommendation
├─ v7   # Pipeline-structured recommendation with API
├─ v8   # Object-oriented recommendation
└─ v10  # Production-ready recommendation, Flask, Docker, testing
```
### How to run any version
```bash
# Clone repo
git clone <your-repo-url>
cd FakeNewsDetector_BiLSTM

# Install dependencies
pip install -r requirements.txt

# Run any version
cd ./<version_folder>
python3 main.py     # interactive CLI & flask
``` 