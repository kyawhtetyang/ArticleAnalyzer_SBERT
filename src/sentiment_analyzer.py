import asyncio
from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self, model_name):
        self.classifier = pipeline("sentiment-analysis", model=model_name)
        self.cache = {}

    async def predict_sentiment_async(self, article_id, text):
        if article_id in self.cache:
            return self.cache[article_id]
        result = self.classifier(text)[0]['label']
        self.cache[article_id] = result
        return result

    async def run(self, df, text_col):
        tasks = [self.predict_sentiment_async(row['articleId'], row[text_col]) for _, row in df.iterrows()]
        df['sentiment'] = await asyncio.gather(*tasks)
        return df


import asyncio
from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self, model_name):
        self.classifier = pipeline("sentiment-analysis", model=model_name)
        self.cache = {}

    async def predict_sentiment_async(self, article_id, text):
        if article_id in self.cache:
            return self.cache[article_id]
        result = self.classifier(text)[0]['label']
        self.cache[article_id] = result
        return result

    async def run(self, df, text_col):
        tasks = [self.predict_sentiment_async(row['articleId'], row[text_col]) for _, row in df.iterrows()]
        df['sentiment'] = await asyncio.gather(*tasks)
        return df


