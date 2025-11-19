import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# ===== 1) Datasetni o‘qish =====
with open("futbol_data_set_savol_javob (1).txt", "r", encoding="utf-8") as f:
    texts = [x.strip() for x in f.readlines() if x.strip()]

k = 3   # nechta klasterga ajratish

# ===== 2) Matnni vektorlash =====
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(texts)

# ===== 3) KMeans klasterlash =====
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X)
labels = kmeans.labels_

# ===== 4) Natijani faylga yozish =====
for cluster_id in range(k):
    fname = f"cluster_{cluster_id}.txt"
    with open(fname, "w", encoding="utf-8") as f:
        for text, label in zip(texts, labels):
            if label == cluster_id:
                f.write(text + "\n")

print("✅ Klasterlash yakunlandi! Fayllar yaratildi.")
