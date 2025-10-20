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

