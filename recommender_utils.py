def hybrid_recommend(title, df, cosine_sim, indices, top_n=10):
    if title not in indices:
        return "Movie not found in database."

    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]  # Exclude the movie itself

    movie_indices = [i[0] for i in sim_scores]
    recommended = df.iloc[movie_indices][['title', 'overview', 'popularity', 'vote_average', 'poster_path']]
    recommended = recommended.sort_values(by='vote_average', ascending=False)
    return recommended
