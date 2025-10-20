# ArticleAnalyzer_SBERT v6

## Features
- Async batch NLP analysis (sentiment)
- Sentence-transformer embeddings for recommendations
- REST API: `/api/analyze` and `/api/recommend`
- Flask web interface with full article analysis (summary, NER, keywords)
- SQLite caching for repeated predictions
- Docker-ready for deployment
- Unit tests for pipeline

## Run
```bash
cd ~/ArticleAnalyzer_SBERT/v6
python3 main.py
export FLASK_APP=app/routes.py
flask run
```
