# 🎬 Hybrid Movie Recommender System

Netflix-style movie recommender built with Streamlit, using TF-IDF + Cosine Similarity. Recommends similar movies based on content and shows top trending movies!
 
![Project Image](https://raw.githubusercontent.com/Rushi430/hybrid-movie-recommender/main/assets/recommender.png)
> UI preview of the hybrid movie recommender system built with Streamlit.


## 🔍 Features
- Content-based filtering using movie overviews
- Popular movies section
- Streamlit frontend with posters and ratings
- Modular code with `recommender_utils.py`

## 📁 Files
- `app.py`: Streamlit frontend
- `recommender_utils.py`: Hybrid recommend function
- `tmdb_movies.csv`: Dataset
- `hybrid_recommender1.pkl`: Saved model
- `requirements.txt`: Python dependencies

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
