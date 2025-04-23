import streamlit as st
import pandas as pd
import pickle
from recommender_utils import hybrid_recommend

with open(r"C:\Users\Admin\Downloads\netflix recommendation system1\hybrid_recommender1.pkl", "rb") as file:
    model_data = pickle.load(file)

cosine_sim = model_data['cosine_sim']
indices = model_data['indices']
df = model_data['df']

def get_poster(path):
    base_url = "https://image.tmdb.org/t/p/w500/"
    return f"{base_url}{path}"

st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Hybrid Movie Recommender System")

movie_list = df['title'].values
title = st.selectbox("Choose a movie to get recommendations", movie_list)

if st.button("Recommend"):
    recommendations = hybrid_recommend(title, df, cosine_sim, indices)
    if isinstance(recommendations, str):
        st.error(recommendations)
    else:
        st.subheader("Top Recommendations")
        cols = st.columns(5)
        for i, row in enumerate(recommendations.head(5).itertuples()):
            with cols[i % 5]:
                st.image(get_poster(row.poster_path), use_column_width=True)
                st.markdown(f"**{row.title}**")
                st.caption(f"⭐ {row.vote_average} | 🔥 {int(row.popularity)}")

st.markdown("---")
st.subheader("🔥 Popular Movies")
popular_movies = df.sort_values("popularity", ascending=False).head(5)
cols = st.columns(5)
for i, row in enumerate(popular_movies.itertuples()):
    with cols[i % 5]:
        st.image(get_poster(row.poster_path), use_column_width=True)
        st.markdown(f"**{row.title}**")
        st.caption(f"⭐ {row.vote_average} | 🔥 {int(row.popularity)}")
