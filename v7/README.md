# ArticleAnalyzer_SBERT v7
## Features
- Async batch NLP analysis (sentiment)
- Sentence-transformer embeddings for recommendations
- REST API (/api/analyze, /api/recommend)
- Flask web interface (summary, NER, keywords)
- SQLite caching for repeated predictions
- Docker-ready
- Unit tests for pipeline
- Minimal CSS/JS frontend styling

## Run
```bash
cd ~/ArticleAnalyzer_SBERT/v7
python3 main.py
export FLASK_APP=app/routes.py
flask run
```

```python
