import pandas as pd
import re
from transformers import pipeline

class NLPEngine:
    def __init__(self, dataset_paths, text_col):
        self.dataset_paths = dataset_paths
        self.text_col = text_col
        self.df = None
        self.ner_clf = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")
        self.summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

    def load_and_clean(self):
        dfs = [pd.read_csv(p) for p in self.dataset_paths]
        df = pd.concat(dfs, ignore_index=True)
        df = df.dropna(subset=[self.text_col])
        df = df[df[self.text_col].apply(lambda x: isinstance(x, str))]
        df['clean_content'] = df[self.text_col].apply(
            lambda x: re.sub(r'\s+', ' ', x.strip()) if isinstance(x, str) else ''
        )
        self.df = df
        return self.df

    def extract_keywords(self, top_k=5):
        stopwords = set(['the', 'and', 'of', 'in', 'a', 'to', 'for', 'that', 'with'])
        keywords_list = []
        for text in self.df[self.text_col]:
            words = [w.lower() for w in re.findall(r'\w+', text) if w.lower() not in stopwords]
            freq = {}
            for w in words:
                freq[w] = freq.get(w, 0) + 1
            kws = sorted(freq, key=freq.get, reverse=True)[:top_k]
            keywords_list.append(kws)
        self.df['keywords'] = keywords_list
        return self.df

    def add_ner_summary(self):
        self.df['ner'] = self.df[self.text_col].apply(lambda t: self.ner_clf(t))

        def summarize_text(t):
            text_len = len(t.split())
            min_len = min(text_len, 5)
            max_len = min(text_len + 3, 8)
            return self.summarizer(t, max_length=max_len, min_length=min_len, do_sample=False)[0]['summary_text']

        self.df['summary'] = self.df[self.text_col].apply(summarize_text)
        return self.df

    def run(self):
        self.load_and_clean()
        self.extract_keywords()
        self.add_ner_summary()
        return self.df


import pandas as pd
import re
from transformers import pipeline

class NLPEngine:
    def __init__(self, dataset_paths, text_col):
        self.dataset_paths = dataset_paths
        self.text_col = text_col
        self.df = None
        self.ner_clf = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")
        self.summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

    def load_and_clean(self):
        dfs = [pd.read_csv(p) for p in self.dataset_paths]
        df = pd.concat(dfs, ignore_index=True)
        df = df.dropna(subset=[self.text_col])
        df = df[df[self.text_col].apply(lambda x: isinstance(x, str))]
        df['clean_content'] = df[self.text_col].apply(
            lambda x: re.sub(r'\s+', ' ', x.strip()) if isinstance(x, str) else ''
        )
        self.df = df
        return self.df

    def extract_keywords(self, top_k=5):
        stopwords = set(['the', 'and', 'of', 'in', 'a', 'to', 'for', 'that', 'with'])
        keywords_list = []
        for text in self.df[self.text_col]:
            words = [w.lower() for w in re.findall(r'\w+', text) if w.lower() not in stopwords]
            freq = {}
            for w in words:
                freq[w] = freq.get(w, 0) + 1
            kws = sorted(freq, key=freq.get, reverse=True)[:top_k]
            keywords_list.append(kws)
        self.df['keywords'] = keywords_list
        return self.df

    def add_ner_summary(self):
        self.df['ner'] = self.df[self.text_col].apply(lambda t: self.ner_clf(t))

        def summarize_text(t):
            text_len = len(t.split())
            min_len = min(text_len, 5)
            max_len = min(text_len + 3, 8)
            return self.summarizer(t, max_length=max_len, min_length=min_len, do_sample=False)[0]['summary_text']

        self.df['summary'] = self.df[self.text_col].apply(summarize_text)
        return self.df

    def run(self):
        self.load_and_clean()
        self.extract_keywords()
        self.add_ner_summary()
        return self.df


