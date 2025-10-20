# ArticleAnalyzer_SBERT v1

## Features
- CSV dataset loading
- Text preprocessing
- Hugging Face sentiment analysis (DistilBERT)
- Modular pipeline
- Flask web interface: view articles & sentiment
- Clean, extendable structure

## Run
```bash
cd ~/ArticleAnalyzer_SBERT/v1
python3 main.py
export FLASK_APP=app/routes.py
flask run

```
