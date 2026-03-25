import string
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def clean_text(text):
  
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    cleaned_words = [word for word in words if word not in ENGLISH_STOP_WORDS]
    return " ".join(cleaned_words)

sample_text = "Hello!!! This is a simple TEXT cleaning example, and it works great."

cleaned = clean_text(sample_text)

print("Original Text:")
print(sample_text)

print("\nCleaned Text:")
print(cleaned)