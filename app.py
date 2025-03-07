import streamlit as st
from tensorflow.keras.models import load_model
import joblib
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the trained model and tokenizer
model = load_model("model.h5")
tokenizer = joblib.load("tokenizer.pkl")


# Function to make predictions
def predictive_system(review):
    sequences = tokenizer.texts_to_sequences([review])
    padded_sequence = pad_sequences(sequences, maxlen=200)
    prediction = model.predict(padded_sequence)
    sentiment = "😊 Positive" if prediction[0][0] > 0.5 else "😞 Negative"
    return sentiment


# Streamlit UI
st.title("🎬 Movie Sentiment Analysis Application")

st.write(
    "Enter a movie review below, and the model will predict whether it's positive or negative."
)

# User input
review = st.text_area("Enter your movie review here:")

if st.button("Analyze Sentiment"):
    if review.strip():
        sentiment = predictive_system(review)
        st.success(f"Predicted Sentiment: {sentiment}")
    else:
        st.warning("Please enter a review to analyze.")
