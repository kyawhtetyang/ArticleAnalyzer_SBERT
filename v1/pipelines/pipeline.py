import json
from src.preprocessing import clean_text
from src.sentiment_model import load_sentiment_model, predict_sentiment
from src.utils import load_dataset, add_clean_column

def full_pipeline(config: dict):
    df = load_dataset(config["dataset_path"])
    df = add_clean_column(df, config.get("text_col","content"), clean_text)

    classifier = load_sentiment_model(config.get("model_name"))
    df['sentiment'] = predict_sentiment(classifier, df['clean_content'].tolist())
    return df

