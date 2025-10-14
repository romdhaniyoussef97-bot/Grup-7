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
    
    # The API takes id's to identify genres. Since the user doesn't know what each
    # genre have we need a function to translate from text to id 
    def genre_query(self, genre_string):
        if not genre_string:
            return None
        
        genre_map = {val["name"].lower(): val["id"] for val in self.genres}
        genre_ids = [str(genre_map[name]) for name in genre_string.lower().split() if name in genre_map]
        
        return(",".join(genre_ids))
    
    # Function to send avaiable genres to the user
    def get_genres(self):
        genre_list = [genre['name'] for genre in self.genres]
        return (genre_list)

    # The API doesn't have any random-function, hence we need to build one.
    # We start by looking at the number of pages that exists given a specific query
    # We then randomize a value from 1 to min(500, max_pages). 500 is the highest
    # value the API accepts. 

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
            query_params['page'] = min(random_page, 500)
            
            respons = requests.get(
                url = base_url,
                headers=self.header,
                params=query_params
            ).json()['results']
            
            movie = random.choice(respons)

            return {
                "title" : movie.get('title', "No title available."),
                "rating" : movie.get('vote_average', "No average available."),
                "releas_date" : movie.get("release_date", "No realase date available."),
                "genre" : [val['name'] for val in self.genres if val['id'] in movie.get("genre_ids", [])],
                "plot" : movie.get("overview", "No plot available.")
            }
    
        except Exception as e:
            return f"Failed to find movie. Exception : {e}"
            
