from src.nlp_utils import load_dataset, add_clean_column, enrich_articles

def full_pipeline(config: dict):
    df = load_dataset(config["dataset_path"])
    df = add_clean_column(df, config.get("text_col","content"))
    df = enrich_articles(df,
            sentiment_model=config.get("sentiment_model"),
            ner_model=config.get("ner_model"),
            summarization_model=config.get("summarization_model"))
    return df

