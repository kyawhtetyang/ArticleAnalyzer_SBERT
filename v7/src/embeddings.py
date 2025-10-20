from sentence_transformers import SentenceTransformer
import numpy as np

def get_embeddings(texts, model_name="sentence-transformers/all-MiniLM-L6-v2"):
    model = SentenceTransformer(model_name)
    return model.encode(texts, convert_to_numpy=True)

def cosine_similarity_matrix(embeddings):
    norm = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
    return np.dot(norm, norm.T)

