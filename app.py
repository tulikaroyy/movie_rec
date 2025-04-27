import streamlit as st
import pickle
import pandas as pd
import requests
import gdown
import os

# Set background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://drive.google.com/uc?export=view&id=1OcdVbcG4AjpEdRb62JvMRE2VYH2fQJ_d");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Shift content more towards the left
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 1rem;
        padding-right: 1rem;
        text-align: left;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Download files from Google Drive if not already present
if not os.path.exists('movie_dict.pkl'):
    url = 'https://drive.google.com/uc?id=1FoZwpaGO28UEiytbr3NWtJlpROynXs_0'
    gdown.download(url, 'movie_dict.pkl', quiet=False)

if not os.path.exists('similarity.pkl'):
    url = 'https://drive.google.com/uc?id=12ra6C_3AZf2Y_OV6vBtSE_Tfjpz00dHR'
    gdown.download(url, 'similarity.pkl', quiet=False)

# Load the files
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to fetch poster (placeholder for now)
def fetch_poster(movie_id):
    return "https://via.placeholder.com/150"  # you can improve later

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Streamlit UI
st.title('Movie Recommender System')

selected_movie_name = st.selectbox('What movie would you like to watch?', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.subheader('Recommended Movies:')
    for movie in recommendations:
        st.write(movie)

