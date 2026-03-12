
import pickle
from schema.input import input_movie

with open('model/similarity.pkl','rb') as f:
   similarity=pickle.load(f) 


with open('model/movies_data.pkl','rb')as f:
    data=pickle.load(f)




def movie_recommend(movie_title:str, top_n:int):

    movie_title = movie_title.lower().strip()

    titles = data['title'].str.lower().str.strip()

    if movie_title not in titles.values:
        return {
            "query_movie": movie_title,
            "recommendations": [],
            "message": "Movie not found"
        }

    idx = titles[titles == movie_title].index[0]

    sim_scores = list(enumerate(similarity[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:50]

    movie_indices = [i[0] for i in sim_scores]

    recommended = data.iloc[movie_indices]

    recommended = recommended.sort_values(
        by='popularity_score',
        ascending=False
    )

    recommended = recommended[['movieId','title','average_rating','rating_count']].head(top_n)

    return {
        "query_movie": movie_title,
        "recommendations": recommended.to_dict(orient="records")
    }



