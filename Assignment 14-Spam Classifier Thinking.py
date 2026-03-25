
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


data = {
    "message": [
        "Win a free iPhone now",
        "Limited time offer click now",
        "Meeting at 5 pm",
        "Let's have lunch tomorrow",
        "Claim your prize now",
        "Project submission deadline"
    ],
    "label": [1, 1, 0, 0, 1, 0]  # 1 = Spam, 0 = Not Spam
}

df = pd.DataFrame(data)


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["message"])

y = df["label"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


model = MultinomialNB()
model.fit(X_train, y_train)

test_msg = ["Free offer just for you"]
test_data = vectorizer.transform(test_msg)

prediction = model.predict(test_data)

if prediction[0] == 1:
    print("Spam Message")
else:
    print("Not Spam")





1 Features for Spam Detection

Features are the inputs used by the ML model to decide whether a message is spam.

Text-Based Features
*Number of spam keywords (e.g., “free”, “win”, “offer”)
*Message length
*Presence of links (URLs)
*Use of capital letters (e.g., “URGENT!!!”)
*Special characters (!!!, $$$)

Sender-Based Features
Unknown or suspicious sender
Sender frequency (new vs frequent contact)
Email/domain reputation
Behavioral Features
Number of messages sent in short time
Whether user previously marked similar messages as spam


2 Dataset Requirements
Collection of messages/emails
Each message labeled as:
Spam (1)
Not Spam (0)
Example Dataset
Message	Label
"Win a free iPhone now!!!"	Spam
"Meeting at 3 PM"	Not Spam
"Limited time offer, click now"	Spam


3 Possible Mistakes (Errors)
 False Positive
Normal message marked as spam
Example: “Free notes available for exam”
False Negative
Spam message marked as normal
Example: “You won prize, claim now”