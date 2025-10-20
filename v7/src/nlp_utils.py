import pandas as pd
import re
import asyncio

def load_dataset(path):
    return pd.read_csv(path)

def add_clean_column(df, text_col):
    df['clean_content'] = df[text_col].apply(lambda x: re.sub(r'\s+', ' ', x.strip()))
    return df

async def predict_sentiment_async(classifier, article_id, text):
    # async wrapper for pipeline
    return classifier(text)[0]['label']

def extract_keywords(series, top_k=5):
    # naive keywords: top_k frequent words ignoring stopwords
    stopwords = set(['the','and','of','in','a','to','for','that','with'])
    keywords_list = []
    for text in series:
    # texts = ["i love u. i hate u and i miss u."]
        words = [w.lower() for w in re.findall(r'\w+', text) if w.lower() not in stopwords]
        # ['i','love','u','i','hate','u','i','miss','u']
        freq = {}
        for w in words: freq[w] = freq.get(w,0)+1
        # {'i':3, 'u':3, 'love':1, 'hate':1, 'miss':1}
        kws = sorted(freq, key=freq.get, reverse=True)[:top_k]
        # print(sorted(words, key=len))
        # ['i','u','love','hate','miss']
        keywords_list.append(kws)
        # [['i','u','love','hate','miss']]
    return keywords_list

def init_db():
    # placeholder for caching/db
    return True

