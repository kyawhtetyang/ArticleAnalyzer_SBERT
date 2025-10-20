import re
import pandas as pd
from transformers import pipeline

# -------------------
# Text preprocessing
# -------------------
def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# -------------------
# Dataset helpers
# -------------------
def load_dataset(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def add_clean_column(df: pd.DataFrame, text_col: str) -> pd.DataFrame:
    df['clean_content'] = df[text_col].apply(clean_text)
    return df

# -------------------
# Hugging Face models
# -------------------
def load_pipeline(task: str, model_name: str):
    return pipeline(task, model=model_name)

def predict_sentiment(classifier, texts):
    return [classifier(t)[0]['label'] for t in texts]

def predict_ner(classifier, texts):
    return [classifier(t) for t in texts]


def predict_summary(classifier, texts):
    summaries = []
    for t in texts:  # loop at the top
        summary = classifier(
            t,
            max_length=min(len(t.split()) + 3, 8),  # dynamic max length
            min_length=min(len(t.split()), 5),      # dynamic min length
            do_sample=False
        )[0]['summary_text']
        summaries.append(summary)
    return summaries


# -------------------
# Combine predictions
# -------------------
def enrich_articles(df, sentiment_model, ner_model, summarization_model):
    sentiment_clf = load_pipeline("sentiment-analysis", sentiment_model)
    ner_clf = load_pipeline("ner", ner_model)
    summarization_clf = load_pipeline("summarization", summarization_model)

    df['sentiment'] = predict_sentiment(sentiment_clf, df['clean_content'].tolist())
    df['ner'] = predict_ner(ner_clf, df['clean_content'].tolist())
    df['summary'] = predict_summary(summarization_clf, df['clean_content'].tolist())
    return df

