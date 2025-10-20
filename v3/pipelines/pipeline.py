from src.preprocessing import clean_text
from src.sentiment_model import load_sentiment_model, predict_sentiment
from src.ner_model import load_ner_model, predict_entities
from src.summarizer_model import load_summarizer, summarize_text
from src.keywords_model import extract_keywords
from src.utils import load_dataset, add_clean_column

def full_pipeline(config: dict):
    df = load_dataset(config["dataset_path"])
    df = add_clean_column(df, config.get("text_col","content"), clean_text)

    # Sentiment
    sentiment_model = load_sentiment_model(config.get("sentiment_model_name"))
    df['sentiment'] = predict_sentiment(sentiment_model, df['clean_content'].tolist())

    # NER
    ner_model = load_ner_model(config.get("ner_model_name"))
    df['entities'] = predict_entities(ner_model, df['clean_content'].tolist())

    # Summarization
    summarizer = load_summarizer(config.get("summarizer_model_name"))
    df['summary'] = summarize_text(summarizer, df['clean_content'].tolist())

    # Keywords
    df['keywords'] = extract_keywords(df['clean_content'].tolist(), top_k=config.get("top_k_keywords",5))

    return df

