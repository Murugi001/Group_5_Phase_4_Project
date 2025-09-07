# train_pipeline.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
import joblib

# Example dataset (replace with your own)
data = pd.DataFrame({
    "tweet": [
        "I love apple",
        "I hate banana",
        "This phone is okay",
        "I don't like apple",
        "Best day ever!",
        "Worst experience ever"
    ],
    "sentiment": ["Positive", "Negative", "Neutral", "Negative", "Positive", "Negative"]
})

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    data["tweet"], data["sentiment"], test_size=0.2, random_state=42
)

# Build pipeline: TF-IDF + SVM
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english")),
    ("clf", SVC(kernel="linear", probability=True))   # probability=True for confidence scores
])

# Fit pipeline
pipeline.fit(X_train, y_train)

# Save fitted pipeline
joblib.dump(pipeline, "svm_nlp_pipeline.pkl")

print("✅ Pipeline trained and saved as svm_nlp_pipeline.pkl")