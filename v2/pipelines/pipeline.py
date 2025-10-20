from src.preprocessing import clean_text
from src.sentiment_model import load_sentiment_model, predict_sentiment
from src.ner_model import load_ner_model, predict_entities
from src.utils import load_dataset, add_clean_column
import json

def full_pipeline(config: dict):
    df = load_dataset(config["dataset_path"])
    df = add_clean_column(df, config.get("text_col","content"), clean_text)

    # Sentiment
    sentiment_model = load_sentiment_model(config.get("sentiment_model_name"))
    df['sentiment'] = predict_sentiment(sentiment_model, df['clean_content'].tolist())

    # NER (for demo, just first text)
    ner_model = load_ner_model()
    df['entities'] = predict_entities(ner_model, df['clean_content'].tolist())

    return df

