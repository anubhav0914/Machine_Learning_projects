import pickle
import pandas as pd
import streamlit as st
import requests


movies_dict= pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=9b44acf9fea04c6ae068f675bab3077f&language=en-US"

    response = requests.get(url)
    data = response.json()
    path = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    return path


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    # using enumarte function to don't miss the index (enmrate we create a touple of with index )

    moive_list = sorted(enumerate(distance), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies =[]
    recommend_movies_poster = []
    for i in moive_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies,recommend_movies_poster



similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')

Selected_movie = st.selectbox(
    'Give the movie name ,which is currently you watched ',
    (movies['title'].values)
)

if st.button('Recommend'):
    name , poster = recommend(Selected_movie)
    st.write(name)

    col1 ,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col1:
        st.text(name[1])
        st.image(poster[1])
    with col2:
        st.text(name[2])
        st.image(poster[2])
    with col3:
        st.text(name[3])
        st.image(poster[3])
    with col4:
        st.text(name[4])
        st.image(poster[4])