from nltk.corpus import wordnet as wn
import nltk

nltk.download('wordnet')

word_pairs = [
    ("car", "automobile"),
    ("happy", "joyful"),
    ("big", "large"),
    ("fast", "quick"),
    ("smart", "intelligent")
]

for w1, w2 in word_pairs:
    syn1 = wn.synsets(w1)
    syn2 = wn.synsets(w2)

    if syn1 and syn2:
        similarity = syn1[0].wup_similarity(syn2[0])
        print(f"{w1} - {w2} similarity:", round(similarity, 2))