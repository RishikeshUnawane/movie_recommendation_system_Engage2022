########################################################################################################################################################################
#                                                                 MOVIE RECOMMENDATION SYSTEM                                                                          #
########################################################################################################################################################################

# importing all the necessary libraries
import pandas as pd
import streamlit as st
import pickle 
import requests

# loading the model
st.header('Movie Recommender System')
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

# helper function to fetch poster of the movies using the movie id
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# main function for recommending top 10 movies to the user based on the similarity score
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names,recommended_movie_posters

# select box and search bar provided to the user to search the movies
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# A button to recommend movies to the user
# if the user selects some movie and clicks on the recommend button it will show him top 10 movies similar to the selected movie
if st.button('Recommend'):
    st.header('Top 5 recommended movies are:')  # first it will display the top 5 most similar movies
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    st.header('Some other options:') # next user will see movies less similar to the selected movie
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
    with col2:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])
    with col3:
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])
    with col4:
        st.text(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])
    with col5:
        st.text(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])

########################################################################################################################################################################
#                                                                                END                                                                                   #
########################################################################################################################################################################
