import os
import requests
import random

from dotenv import load_dotenv
from pathlib import Path

class TMDB_API: 
    def __init__(self):
        env_path = Path(__file__).resolve().parent.parent / ".env"
        load_dotenv(dotenv_path=env_path)
        self.API_KEY = os.getenv("API_KEY")
        self.header = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.API_KEY}"
        }
        
        self.genres = requests.get(
            url = "https://api.themoviedb.org/3/genre/movie/list?language=en",
            headers=self.header
        ).json()["genres"]
        
    def genre_query(self, genre_string):
        if not genre_string:
            return None
        
        genre_map = {val["name"].lower(): val["id"] for val in self.genres}
        genre_ids = [str(genre_map[name]) for name in genre_string.lower().split() if name in genre_map]
        
        return(",".join(genre_ids))
    
    def get_genres(self):
        genre_list = [genre['name'] for genre in self.genres]
        return (genre_list)

    def get_random_movie(self, 
                         release_date_gte = None,
                         include_adult = None, 
                         vote_average_gte = None,
                         genre = None):
        
        base_url = "https://api.themoviedb.org/3/discover/movie?"
        
        query_params = {
            "release_date.gte" : release_date_gte,
            "include_adult" : include_adult,
            "vote_average.gte" : vote_average_gte,
            "with_genres" : self.genre_query(genre),
            "page" : 1
        }
        
        try:
            total_pages = requests.get(
                url = base_url,
                headers=self.header,
                params=query_params
            ).json()['total_pages']
            
            random_page = random.randint(1, total_pages)
            
            query_params['page'] = random_page
            
            respons = requests.get(
                url = base_url,
                headers=self.header,
                params=query_params
            ).json()['results']
            
            movie = random.choice(respons)
            return {
                "title" : movie.get('title', "No title available."),
                "rating" : movie.get('vote_average', "No average avaiable."),
                "releas_date" : movie.get("release_date", "No realase date available."),
                "genre" : [],
                "plot" : movie.get("overview", "No plot avaiable.")
            }
    
        except Exception as e:
            return f"Failed to find movie. Exception : {e}"
            