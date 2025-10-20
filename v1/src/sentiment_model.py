from transformers import pipeline

def load_sentiment_model(model_name: str = "distilbert-base-uncased-finetuned-sst-2-english"):
    """Load Hugging Face sentiment analysis pipeline."""
    return pipeline("sentiment-analysis", model=model_name)

def predict_sentiment(classifier, texts):
    """Return sentiment label for list of texts."""
    return [classifier(t)[0]['label'] for t in texts]

