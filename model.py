import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Load data
df = pd.read_csv("data.csv")

X = df["text"]
y = df["category"]

# Create model pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", MultinomialNB())
])

# Train model
model.fit(X, y)

# Function to use model (IMPORTANT for Streamlit)
def predict_category(text):
    return model.predict([text])[0]

