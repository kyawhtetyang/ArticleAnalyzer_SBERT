from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

class EmbeddingEngine:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.ids = []

    def encode(self, texts):
        return self.model.encode(texts, convert_to_numpy=True)

    def build_index(self, embeddings, ids):
        self.ids = ids
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dim)
        self.index.add(embeddings.astype(np.float32))

    def search(self, emb, top_k=3):
        D, I = self.index.search(emb.astype(np.float32), top_k)
        results = [[self.ids[i] for i in row] for row in I]
        return results

    def recommend(self, df, top_n=3):
        embeddings = self.encode(df['clean_content'].tolist())
        self.build_index(embeddings, df['articleId'].tolist())
        recs = {}
        for idx, articleId in enumerate(df['articleId']):
            emb = embeddings[idx:idx+1]
            top_ids = self.search(emb, top_k=top_n+1)[0][1:]
            recs[articleId] = df[df['articleId'].isin(top_ids)][['articleId','title','summary','keywords']].to_dict(orient='records')
        return recs


from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

class EmbeddingEngine:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.ids = []

    def encode(self, texts):
        return self.model.encode(texts, convert_to_numpy=True)

    def build_index(self, embeddings, ids):
        self.ids = ids
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dim)
        self.index.add(embeddings.astype(np.float32))

    def search(self, emb, top_k=3):
        D, I = self.index.search(emb.astype(np.float32), top_k)
        results = [[self.ids[i] for i in row] for row in I]
        return results

    def recommend(self, df, top_n=3):
        embeddings = self.encode(df['clean_content'].tolist())
        self.build_index(embeddings, df['articleId'].tolist())
        recs = {}
        for idx, articleId in enumerate(df['articleId']):
            emb = embeddings[idx:idx+1]
            top_ids = self.search(emb, top_k=top_n+1)[0][1:]
            recs[articleId] = df[df['articleId'].isin(top_ids)][['articleId','title','summary','keywords']].to_dict(orient='records')
        return recs


