import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Load dataset
df = pd.read_csv("data.csv")

X = df["text"]
y = df["category"]

# Model pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", MultinomialNB())
])

# Train model
model.fit(X, y)


# Predict function (WITH confidence)
def predict_category(text):
    probs = model.predict_proba([text])[0]
    prediction = model.predict([text])[0]
    confidence = max(probs)

    return prediction, confidence
