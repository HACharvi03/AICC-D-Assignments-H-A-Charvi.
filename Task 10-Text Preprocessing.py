import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

text = "This is a simple example for text preprocessing in Python!"

# Lowercase
text = text.lower()

# Tokenization
words = word_tokenize(text)

# Remove punctuation
words = [w for w in words if w not in string.punctuation]

# Remove stopwords
stop_words = set(stopwords.words("english"))
words = [w for w in words if w not in stop_words]

print("Processed Text:", words)