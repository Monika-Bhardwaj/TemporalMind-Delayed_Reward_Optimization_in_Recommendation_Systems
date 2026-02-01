import pandas as pd

def load_movielens_1m():
    ratings = pd.read_csv(
        "data/raw/ratings.dat",
        sep="::",
        engine="python",
        names=["user_id", "movie_id", "rating", "timestamp"]
    )

    users = pd.read_csv(
        "data/raw/users.dat",
        sep="::",
        engine="python",
        names=["user_id", "gender", "age", "occupation", "zip"]
    )

    movies = pd.read_csv(
        "data/raw/movies.dat",
        sep="::",
        engine="python",
        names=["movie_id", "title", "genres"]
    )

    ratings["datetime"] = pd.to_datetime(ratings["timestamp"], unit="s")
    return ratings, users, movies
