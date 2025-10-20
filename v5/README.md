# ArticleAnalyzer_SBERT v5

## Features
- CSV dataset loading
- Text preprocessing
- Multi-task NLP: sentiment, NER, summarization
- Keyword extraction & content similarity
- Recommendations via cosine similarity
- Modular pipeline (nlp_utils + pipeline)
- SQLite database storage
- Flask web interface with analysis & recommendations pages
- Clean, extendable, user-friendly project

## Run
```bash
cd ~/ArticleAnalyzer_SBERT/v5
python3 main.py
export FLASK_APP=app/routes.py
flask run

```
