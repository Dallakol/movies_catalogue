import requests

Params = {'api_key': "6e89108b31917285ff3ea718c172809d"}

def get_movies_list(list_type):
    url = f"https://api.themoviedb.org/3/movie/{list_type}"
    params = Params
    response = requests.get(url, params = params)
    response.raise_for_status()
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_single_movie(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = Params
    response = requests.get(url, params=params)
    return response.json()

def get_single_movie_cast(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    params = Params
    response = requests.get(url, params=params)
    return response.json()["cast"]

def get_movie_images(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    params = Params
    response = requests.get(url, params = params)
    return response.json()


