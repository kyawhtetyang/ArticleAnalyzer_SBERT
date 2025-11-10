import asyncio
from src.nlp_engine import NLPEngine
from src.embedding_engine import EmbeddingEngine
from src.sentiment_analyzer import SentimentAnalyzer
from src.clusterer import Clusterer

class NewsPipeline:
    def __init__(self, config):
        self.config = config
        self.df = None
        self.recs = None
        self.nlp_engine = NLPEngine(config["dataset_paths"], config["text_col"])
        self.embedding_engine = EmbeddingEngine(config.get("embedding_model"))
        self.sentiment_analyzer = SentimentAnalyzer(config.get("model_name"))
        self.clusterer = Clusterer(config.get("n_clusters",3))

    def run_full_pipeline(self):
        # NLP
        self.df = self.nlp_engine.run()
        # Sentiment
        asyncio.get_event_loop().run_until_complete(self.sentiment_analyzer.run(self.df, self.config["text_col"]))
        # Embeddings & Recommendations
        self.recs = self.embedding_engine.recommend(self.df, top_n=self.config.get("top_n",3))
        # Clustering
        embeddings = self.embedding_engine.encode(self.df['clean_content'].tolist())
        self.df['cluster'] = self.clusterer.run(embeddings)
        return self.df, self.recs

import asyncio
from src.nlp_engine import NLPEngine
from src.embedding_engine import EmbeddingEngine
from src.sentiment_analyzer import SentimentAnalyzer
from src.clusterer import Clusterer

class NewsPipeline:
    def __init__(self, config):
        self.config = config
        self.df = None
        self.recs = None
        self.nlp_engine = NLPEngine(config["dataset_paths"], config["text_col"])
        self.embedding_engine = EmbeddingEngine(config.get("embedding_model"))
        self.sentiment_analyzer = SentimentAnalyzer(config.get("model_name"))
        self.clusterer = Clusterer(config.get("n_clusters",3))

    def run_full_pipeline(self):
        # NLP
        self.df = self.nlp_engine.run()
        # Sentiment
        asyncio.get_event_loop().run_until_complete(self.sentiment_analyzer.run(self.df, self.config["text_col"]))
        # Embeddings & Recommendations
        self.recs = self.embedding_engine.recommend(self.df, top_n=self.config.get("top_n",3))
        # Clustering
        embeddings = self.embedding_engine.encode(self.df['clean_content'].tolist())
        self.df['cluster'] = self.clusterer.run(embeddings)
        return self.df, self.recs

