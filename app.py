import streamlit as st
import pickle
import pandas as pd
import streamlit as st
import pickle
import pandas as pd
import requests
import gdown
import os

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

def fetch_poster(movie_id):
    return "https://via.placeholder.com/150"  # Placeholder (you can improve later)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Streamlit UI
st.title('Movie Recommender System')

selected_movie_name = st.selectbox('What movie would you like to watch?', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
