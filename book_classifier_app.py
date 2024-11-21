
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load model and vectorizer
with open('book_classifier_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

with open("encoder.pkl", "rb") as encoder_file:
    encoder = pickle.load(encoder_file)

# Function to predict genre based on description
def predict_genre(description):
    description_vectorized = vectorizer.transform([description])
    genre = model.predict(description_vectorized)
    return genre[0]

# Streamlit app
st.title('Classificador de Gêneros de Livros')
st.write("Digite a descrição de um livro e descubra seu gênero!")

# User input for book description
description = st.text_area("Descrição do Livro:")

if st.button('Classificar'):
    if description:
        genre = encoder.inverse_transform([predict_genre(description)])[0]
        st.write(f"O gênero do livro é: {genre}")
    else:
        st.write("Por favor, insira uma descrição.")
    
