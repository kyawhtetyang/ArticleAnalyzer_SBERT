from transformers import pipeline

def load_sentiment_model(model_name: str):
    return pipeline("sentiment-analysis", model=model_name)

def predict_sentiment(classifier, texts):
    return [classifier(t)[0]['label'] for t in texts]

