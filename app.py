import streamlit as st
import pickle
import pandas
import requests

movie_list = pickle.load(open('movie.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
list_movie = movie_list['title'].values

st.title('Movie Recommender System')

def fetch_poster(movie):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie))
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500" + poster_path
    return full_path

def recommend(movie):
    movie_index = movie_list[movie_list['title'] == movie].index[0]
    data = similarity[movie_index]
    listed = list(enumerate(data)) # to preserve the index and the values together
    top_5 = sorted(listed, reverse=True, key=lambda x:x[1])[:6] # the lambda function will sort based on the value and not the index
    recommended_movies = []
    recommendation_poster = []

    for i in top_5:
        movie_id = i[0]
        recommended_movies.append(movie_list.iloc[i[0]].title)

        #fetch poster from API
        tmdb_id = movie_list.iloc[i[0]].movie_id  # get actual TMDB movie ID
        recommendation_poster.append(fetch_poster(tmdb_id))

    
    return(recommended_movies, recommendation_poster)

option = st.selectbox('Tell me your favourite movie',list_movie)
if st.button('Recommend'):
    recommendation, poster = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommendation[0])
        st.image(poster[0])
    with col2:
        st.text(recommendation[1])
        st.image(poster[1])
    with col3:
        st.text(recommendation[2])
        st.image(poster[2])
    with col4:
        st.text(recommendation[3])
        st.image(poster[3])
    with col5:
        st.text(recommendation[4])
        st.image(poster[4])