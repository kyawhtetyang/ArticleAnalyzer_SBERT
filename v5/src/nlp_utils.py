import re, pandas as pd, sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline

# -------------------
# Text preprocessing
# -------------------
def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def load_dataset(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def add_clean_column(df: pd.DataFrame, text_col: str) -> pd.DataFrame:
    df['clean_content'] = df[text_col].apply(clean_text)
    return df

# -------------------
# Hugging Face pipelines
# -------------------
def load_pipeline(task: str, model_name: str):
    return pipeline(task, model=model_name)

def predict_sentiment(classifier, texts):
    return [classifier(t)[0]['label'] for t in texts]

def predict_ner(classifier, texts):
    return [classifier(t) for t in texts]

def predict_summary(classifier, texts):
    summaries = []
    for t in texts:
        text_len = len(t.split())
        min_len = min(text_len, 5)           # dynamic min length
        max_len = min(text_len + 3, 8)       # dynamic max length
        summary = classifier(
            t,
            max_length=max_len,
            min_length=min_len,
            do_sample=False
        )[0]['summary_text']
        summaries.append(summary)
    return summaries
# -------------------
# Keyword extraction
# -------------------
def extract_keywords(texts, top_k=5):
    vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(texts)
    feature_names = vectorizer.get_feature_names_out()
    keywords_list = []
    for row in tfidf_matrix.toarray():
        top_indices = row.argsort()[-top_k:][::-1]
        keywords_list.append([feature_names[i] for i in top_indices])
    return keywords_list

# -------------------
# Similarity / recommendations
# -------------------
def build_similarity_matrix(texts):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(texts)
    sim_matrix = cosine_similarity(tfidf_matrix)
    return sim_matrix

def get_top_n_similar(sim_matrix, index, top_n=3):
    scores = sim_matrix[index]
    top_indices = scores.argsort()[::-1][1:top_n+1]
    top_scores = [scores[i] for i in top_indices]
    return top_indices.tolist(), top_scores

# -------------------
# Database helpers
# -------------------
def init_db(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS news (
            articleId INTEGER PRIMARY KEY,
            title TEXT,
            content TEXT,
            clean_content TEXT,
            sentiment TEXT,
            summary TEXT,
            ner TEXT
        )
    """)
    conn.commit()
    return conn

def save_to_db(conn, df):
    df_copy = df.copy()
    # Convert list columns to JSON strings
    df_copy['keywords'] = df_copy['keywords'].apply(lambda x: ','.join(x) if isinstance(x, list) else x)
    df_copy['ner'] = df_copy['ner'].apply(lambda x: str(x))
    df_copy.to_sql('news', conn, if_exists='replace', index=False)

# -------------------
# Pipeline helper
# -------------------
def enrich_articles(df, config):
    sentiment_clf = load_pipeline("sentiment-analysis", config.get("sentiment_model"))
    ner_clf = load_pipeline("ner", config.get("ner_model"))
    summarization_clf = load_pipeline("summarization", config.get("summarization_model"))

    df['sentiment'] = predict_sentiment(sentiment_clf, df['clean_content'].tolist())
    df['ner'] = predict_ner(ner_clf, df['clean_content'].tolist())
    df['summary'] = predict_summary(summarization_clf, df['clean_content'].tolist())

    df['keywords'] = extract_keywords(df['clean_content'], top_k=config.get("keyword_top_k",5))

    sim_matrix = build_similarity_matrix(df['clean_content'])

    return df, sim_matrix

