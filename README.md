
# IMDb Movie Review Sentiment Analysis 🎬📊

📌 Project Overview

This project is an NLP-based sentiment analysis system that classifies IMDb movie reviews as positive or negative using Machine Learning. The model is built using LSTM (Long Short-Term Memory) and achieves 88% accuracy on test data. It is deployed as an interactive Streamlit web application for real-time sentiment analysis.


## 🚀 Tools & Technologies Used

*	Programming Language: Python

*	Libraries: TensorFlow, Keras, Scikit-Learn, NLTK, NumPy, Pandas, Matplotlib, Streamlit

*	Model: LSTM (Long Short-Term Memory)

*	Feature Engineering: Tokenization, Stopword Removal, Word Embeddings

*	Deployment: Streamlit Web App

## Features

*	Preprocessing: Tokenization, stopword removal, and text cleaning
    
*	Deep Learning Model: LSTM for improved sentiment understanding
    
*	Graphical Analysis: Training & validation accuracy/loss graphs using Matplotlib

*	Model Evaluation: Achieves 88% accuracy on test data

*	Interactive Streamlit Web App: Users can input movie reviews and get real-time sentiment predictions


## 📂 Project Structure 

📦 imdb-sentiment-analysis  
│-- data/               # Dataset (IMDb movie reviews)  
│-- models/             # Trained model files  
│-- notebooks/          # Jupyter notebooks for EDA & training  
│-- app.py              # Streamlit web app for real-time prediction  
│-- train.py            # Training script  
│-- tokenizer.pkl       # Saved tokenizer for text processing  
│-- model.h5            # Saved deep learning model  
│-- requirements.txt    # Required libraries  
│-- README.md           # Project documentation  

## Installation

Install my-project with npm

1️⃣ Clone the Repository
```
git clone https://github.com/Kubendran29/IMDb-Movie-Review-Sentiment-Analysis.git
cd imdb-sentiment-analysis

```
2️⃣ Install Dependencies
```
pip install -r requirements.txt

```
3️⃣ Run the Streamlit Web App

```
streamlit run app.py

```
## 🎯 Results

* Achieved Accuracy: 88% on IMDb movie reviews dataset
* Model Evaluation: Final loss & accuracy evaluated on test data
* Real-Time Sentiment Prediction: Streamlit app for user-friendly interaction

