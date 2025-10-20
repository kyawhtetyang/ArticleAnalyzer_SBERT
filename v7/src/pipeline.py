import asyncio, pandas as pd
from src.nlp_utils import load_dataset, add_clean_column, predict_sentiment_async, extract_keywords, init_db
from transformers import pipeline
from src.embeddings import get_embeddings, cosine_similarity_matrix
import numpy as np

async def analyze_sentiment(df, text_col, model_name):
    classifier = pipeline("sentiment-analysis", model=model_name)
    tasks = [predict_sentiment_async(classifier, row['articleId'], row[text_col])
             for _, row in df.iterrows()]
    sentiments = await asyncio.gather(*tasks)
    df['sentiment'] = sentiments
    return df

def enrich_articles(df, text_col):
    ner_clf = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

    def summarize_text(text):
        text_len = len(text.split())
        min_len = min(text_len, 5)
        max_len = min(text_len + 3, 8)
        return summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)[0]['summary_text']

    df['ner'] = df[text_col].apply(lambda t: ner_clf(t))
    df['summary'] = df[text_col].apply(summarize_text)
    df['keywords'] = extract_keywords(df[text_col], top_k=5)
    return df

def recommend_articles(df, text_col, top_n=3, model_name="sentence-transformers/all-MiniLM-L6-v2"):
    embeddings = get_embeddings(df[text_col].tolist(), model_name=model_name)
    sim_matrix = cosine_similarity_matrix(embeddings)
    recommendations = {}
    for idx, articleId in enumerate(df['articleId']):
        scores = sim_matrix[idx]
        top_indices = np.argsort(scores)[::-1][1:top_n+1]
        recommendations[articleId] = df.iloc[top_indices][['articleId','title','summary','keywords']].to_dict(orient='records')
    return recommendations

def full_pipeline(config):
    # load datasets chronologically: sample → tech → world
    all_dfs = [load_dataset(p) for p in config["dataset_paths"]]
    df = pd.concat(all_dfs, ignore_index=True)
    df = add_clean_column(df, config.get("text_col","content"))
    init_db()
    loop = asyncio.get_event_loop()
    df = loop.run_until_complete(analyze_sentiment(df, 'clean_content', config.get("model_name")))
    df = enrich_articles(df, 'clean_content')
    recs = recommend_articles(df, 'clean_content', top_n=config.get("top_n",3), model_name=config.get("embedding_model"))
    return df, recs

