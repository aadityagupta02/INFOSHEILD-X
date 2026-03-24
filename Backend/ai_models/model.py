import pandas as pd
import re
import nltk
import pickle

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Download once
import nltk

def safe_nltk_download():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')

    try:
        nltk.data.find('tokenizers/punkt_tab')
    except LookupError:
        nltk.download('punkt_tab')

    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')

safe_nltk_download()

# 🔥 TEXT CLEANING FUNCTION
def clean_text(text):
    text = text.lower()

    # remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # tokenize
    words = text.split()

    # remove stopwords
    words = [w for w in words if w not in stopwords.words('english')]

    return " ".join(words)


# 🔥 LOAD DATASET
df = pd.read_csv("dataset.csv")

# Apply cleaning
df["text"] = df["text"].apply(clean_text)

X = df["text"]
y = df["label"]

# 🔥 TF-IDF (better than CountVectorizer)
vectorizer = TfidfVectorizer(max_features=5000)

X_vec = vectorizer.fit_transform(X)

# 🔥 MODEL (better than naive)
model = LogisticRegression()

model.fit(X_vec, y)

# 🔥 SAVE MODEL
with open("ai_models/model.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)


# 🔥 PREDICTION FUNCTION
def predict_text(text):
    text = clean_text(text)

    X_input = vectorizer.transform([text])

    prediction = model.predict(X_input)[0]
    confidence = max(model.predict_proba(X_input)[0]) * 100

    return {
        "result": "FAKE (AI Generated)" if prediction == 1 else "REAL (Human Written)",
        "confidence_percent": round(confidence, 2)
    }