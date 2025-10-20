# ArticleAnalyzer_SBERT v4

## Features
- CSV dataset loading
- Text preprocessing
- Multi-task NLP: sentiment, NER, summarization (Hugging Face pipelines)
- Modular pipeline (nlp_utils + pipeline)
- Flask web interface with base template
- Clean, extendable, user-friendly project

## Run
```bash
cd ~/ArticleAnalyzer_SBERT/v4
python3 main.py
export FLASK_APP=app/routes.py
flask run

```
