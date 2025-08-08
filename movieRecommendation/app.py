import streamlit as st
import pickle as pkl
import pandas as pd
import numpy as np
movies = pkl.load(open('moviesNew.pkl', 'rb'))
similarities = pkl.load(open('similarityNew.pkl', 'rb'))
moviesdf = pd.read_csv('tmdb_5000_movies.csv')


def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distance = similarities[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key = lambda x: x[1])[1:11]

    recommended_movie = []
    for i in movie_list:
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie

def recommend1(movie):
  # movie = movie.lower().replace(" ", "")
  movie_index = movies[movies['title']==movie].index[0]
  if movie_index==-1:
    print("movie not found")
    return
  distances = similarities[movie_index]
  movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:(x[1], movies.iloc[x[0]]['score']))[1:11]

  recommended_movie = []
  for i in movies_list:
      recommended_movie.append(movies.iloc[i[0]].title)
  return recommended_movie



# a

import re

def extract_genres(s):

    return re.findall(r"'name': '([^']*)'|\"name\": \"([^\"]*)\"", s)

all_genres = set()

for row in moviesdf['genres']:
    if pd.notna(row):
        matches = extract_genres(row)
        for match in matches:

            genre = match[0] or match[1]
            all_genres.add(genre)

unique_genres = sorted(all_genres)


# print(all_genres)


with st.sidebar:
    st.markdown("### 🎯 Filter Options")
    genre_selected = st.selectbox("Select Genre", unique_genres)

# print(genrelist)
# print()
st.title('Movie Recommendation')
selected_movie =  st.selectbox('movie recommendation',movies['title'].values)



if st.button('recommend'):
    recommendations = recommend1(selected_movie)
    for i in recommendations:
        st.write(i)



