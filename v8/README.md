# ArticleAnalyzer_SBERT   v8

## Features
- Async batch NLP analysis (sentiment)
- Sentence-transformer embeddings + FAISS recommendations
- KMeans clustering of articles
- Flask web interface (summary, NER, keywords, clusters)
- REST API (/api/analyze, /api/recommend)
- Modular 5-class pipeline: NLPEngine / EmbeddingEngine / SentimentAnalyzer / Clusterer / NewsPipeline
- Unit tests included

## Run
```bash
cd ~/ArticleAnalyzer_SBERT/v8
python3 main.py
export FLASK_APP=app/routes.py
flask run

```
