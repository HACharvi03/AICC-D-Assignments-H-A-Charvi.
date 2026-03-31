from textblob import TextBlob

reviews = [
    "The movie was amazing and full of action",
    "Worst movie I have ever seen",
    "The plot was interesting but slow",
    "I really loved the acting",
    "The film was boring and too long"
]

for review in reviews:
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print(f"Review: {review}")
    print("Sentiment:", sentiment, "\n")