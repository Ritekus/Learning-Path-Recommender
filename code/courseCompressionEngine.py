from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans

model = SentenceTransformer("all-MiniLM-L6-v2")

def compress_courses(course_descriptions):
    embeddings = model.encode(course_descriptions)
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(embeddings)

    compressed = {}
    for idx, cluster in enumerate(clusters):
        compressed.setdefault(cluster, []).append(course_descriptions[idx])

    return compressed
