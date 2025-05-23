import streamlit as st
import pickle
import pandas as pd
import requests
import gdown
import os

#background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/free-vector/dark-black-background-design-with-stripes_1017-38064.jpg?semt=ais_hybrid&w=740");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#shifting left
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

#Google Drive
if not os.path.exists('movie_dict.pkl'):
    url = 'https://drive.google.com/uc?id=1FoZwpaGO28UEiytbr3NWtJlpROynXs_0'
    gdown.download(url, 'movie_dict.pkl', quiet=False)

if not os.path.exists('similarity.pkl'):
    url = 'https://drive.google.com/uc?id=12ra6C_3AZf2Y_OV6vBtSE_Tfjpz00dHR'
    gdown.download(url, 'similarity.pkl', quiet=False)

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

#fetch poster
def fetch_poster(movie_id):
    return "later"  #maybe later 

#recommend func
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

#UI
st.title('Movie Recommender System')

selected_movie_name = st.selectbox('What movie would you like to watch?', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.subheader('Recommended Movies:')
    for movie in recommendations:
        st.write(movie)

