from sklearn.feature_extraction.text import TfidfVectorizer

# Documents
documents = [
    "Machine learning is used in data analysis and prediction",
    "Data science includes machine learning and statistics",
    "Artificial intelligence and machine learning are related fields",
    "Data analysis helps in making decisions",
    "Statistics and probability are important for data science"
]

# TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

# Get feature names
features = vectorizer.get_feature_names_out()

# Print top words per document
for i, doc in enumerate(X.toarray()):
    print(f"\nDocument {i+1}:")
    top_indices = doc.argsort()[-3:]  # top 3 words
    for index in top_indices:
        print(features[index], ":", round(doc[index], 3))