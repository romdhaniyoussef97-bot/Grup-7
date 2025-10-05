import os
import requests
import random
from dotenv import load_dotenv
from pathlib import Path


class TMDB_API:
    """Handles all interactions with The Movie Database (TMDb) API."""

    def __init__(self):
        env_path = Path(__file__).resolve().parent.parent / ".env"
        load_dotenv(dotenv_path=env_path)

        self.API_KEY = os.getenv("API_KEY")
        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.API_KEY}"
        }

        # Load available genres once at initialization
        self.genres = requests.get(
            url="https://api.themoviedb.org/3/genre/movie/list?language=en",
            headers=self.headers
        ).json()["genres"]

    def create_query(self, **kwargs):
        """Utility: builds query string from keyword arguments."""
        return "&".join(
            [f"{k}={v}" for k, v in kwargs.items() if v is not None]
        )

    def genre_query(self, genre_string):
        """Converts text genres to TMDb IDs."""
        if not genre_string:
            return None

        genre_map = {g["name"].lower(): g["id"] for g in self.genres}
        genre_ids = [
            str(genre_map[name]) for name in genre_string.lower().split()
            if name in genre_map
        ]
        return ",".join(genre_ids) if genre_ids else None

    def get_genres(self):
        """Returns a readable list of genres for the user menu."""
        return [g["name"] for g in self.genres]

    def search_movie(self, title):
        """Searches for a movie by title."""
        base_url = "https://api.themoviedb.org/3/search/movie"
        params = {"query": title, "include_adult": False, "language": "en-US"}

        try:
            response = requests.get(base_url, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()["results"]
            if not data:
                return None
            return data[:5]  # top 5 matches
        except Exception as e:
            print(f"Error while searching for movie: {e}")
            return None

    def get_random_movie(self, genre=None, vote_average_gte=None):
        """Fetches a random movie optionally filtered by genre/rating."""
        base_url = "https://api.themoviedb.org/3/discover/movie?"
        random_page = random.randint(1, 10)

        query_params = {
            "include_adult": False,
            "language": "en-US",
            "page": random_page,
            "vote_average.gte": vote_average_gte,
            "with_genres": self.genre_query(genre),
        }

        try:
            url = base_url + self.create_query(**query_params)
            data = requests.get(url, headers=self.headers).json()["results"]

            if not data:
                return None

            movie = random.choice(data)
            return {
                "title": movie.get("title"),
                "year": movie.get("release_date", "")[:4],
                "genre": genre if genre else "Various",
                "rating": movie.get("vote_average", 0),
                "plot": movie.get("overview", "No description available."),
            }

        except Exception as e:
            print(f"Error fetching random movie: {e}")
            return None