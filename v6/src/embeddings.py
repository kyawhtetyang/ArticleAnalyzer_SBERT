from sentence_transformers import SentenceTransformer
import numpy as np

EMBEDDING_MODELS = {}
def get_embeddings(texts, model_name="sentence-transformers/all-MiniLM-L6-v2"):
    if model_name not in EMBEDDING_MODELS:
        EMBEDDING_MODELS[model_name] = SentenceTransformer(model_name)
    model = EMBEDDING_MODELS[model_name]
    return model.encode(texts, convert_to_numpy=True)

def cosine_similarity_matrix(embeddings):
    norm = np.linalg.norm(embeddings, axis=1, keepdims=True)
    return np.dot(embeddings, embeddings.T) / (norm @ norm.T + 1e-10)

