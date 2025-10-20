import os, sqlite3, re, pandas as pd
from transformers import pipeline
from src.embeddings import get_embeddings, cosine_similarity_matrix

DB_PATH = "models/predictions.db"

# ---------------- Database ----------------
def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS sentiment_cache(
            articleId INTEGER PRIMARY KEY,
            sentiment TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_sentiment_cache(articleId, sentiment):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT OR REPLACE INTO sentiment_cache(articleId, sentiment) VALUES (?,?)",
                 (articleId, sentiment))
    conn.commit()
    conn.close()

def load_sentiment_cache(articleId):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT sentiment FROM sentiment_cache WHERE articleId=?", (articleId,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None

# ---------------- Text preprocessing ----------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def add_clean_column(df, text_col):
    df['clean_content'] = df[text_col].apply(clean_text)
    return df

def load_dataset(path):
    return pd.read_csv(path)

# ---------------- Async Sentiment ----------------
import asyncio
async def predict_sentiment_async(classifier, articleId, text):
    cached = load_sentiment_cache(articleId)
    if cached:
        return cached
    result = classifier(text)[0]['label']
    save_sentiment_cache(articleId, result)
    return result

# ---------------- Keywords ----------------
from sklearn.feature_extraction.text import TfidfVectorizer
def extract_keywords(texts, top_k=5):
    vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(texts)
    feature_names = vectorizer.get_feature_names_out()
    keywords_list = []
    for row in tfidf_matrix.toarray():
        top_indices = row.argsort()[-top_k:][::-1]
        keywords_list.append([feature_names[i] for i in top_indices])
    return keywords_list

