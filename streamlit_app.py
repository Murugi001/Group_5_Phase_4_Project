import streamlit as st
import joblib

# Load fitted pipeline
model = joblib.load("svm_nlp_pipeline.pkl")

st.set_page_config(
    page_title="Tweet Sentiment Classifier",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Tweet Sentiment Classifier")
st.write("This app predicts the sentiment of a tweet as *Positive, **Negative, or **Neutral*.")

# User input
user_input = st.text_area("✍ Enter a tweet:")

if st.button("Classify"):
    if user_input.strip():
        prediction = model.predict([user_input])[0]
        probability = model.predict_proba([user_input]).max()
        st.success(f"Prediction: {prediction}")
        st.info(f"Confidence: {probability:.2f}")
    else:
        st.warning("⚠ Please type a tweet before classifying.")