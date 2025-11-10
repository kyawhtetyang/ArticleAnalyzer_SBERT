from sklearn.cluster import KMeans

class Clusterer:
    def __init__(self, n_clusters=3):
        self.n_clusters = n_clusters

    def run(self, embeddings):
        kmeans = KMeans(n_clusters=self.n_clusters, random_state=42)
        clusters = kmeans.fit_predict(embeddings)
        return clusters


from sklearn.cluster import KMeans

class Clusterer:
    def __init__(self, n_clusters=3):
        self.n_clusters = n_clusters

    def run(self, embeddings):
        kmeans = KMeans(n_clusters=self.n_clusters, random_state=42)
        clusters = kmeans.fit_predict(embeddings)
        return clusters


