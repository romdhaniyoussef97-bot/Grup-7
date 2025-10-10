from api.tmdb_api import TMDB_API
from models.movie_model import Movie
from storage.repo import FavoritesManager

class App:
    def __init__(self):
        self.api = TMDB_API()
        self.fav_manager = FavoritesManager("data/favorites.json")
        self.running = True

    def run(self):
        while self.running:
            print("\n=== MOVIE RECOMMENDER ===")
            print("1. Hämta slumpmässig film (med genreval)")
            print("2. Visa favoriter")
            print("3. Redigera favoriter")
            print("0. Avsluta")

            choice = input("\nVälj ett alternativ: ").strip()

            if choice == "1":
                self.random_movie_flow()
            elif choice == "2":
                self.show_favorites()
            elif choice == "3":
                self.edit_favorites()
            elif choice == "0":
                print("Programmet avslutas.")
                self.running = False
            else:
                print("Ogiltigt val, försök igen.")

    def random_movie_flow(self):
        genres = self.api.get_genres()
        print("\nTillgängliga genrer:")
        for i, g in enumerate(genres, start=1):
            print(f"{i}. {g}")

        selected = input("\nAnge genrens nummer (flera nummer separerade med mellanslag, eller tryck Enter för slumpad): ").strip()
        if selected:
            try:
                indexes = [int(x) - 1 for x in selected.split()]
                chosen_genres = [genres[i] for i in indexes if 0 <= i < len(genres)]
            except ValueError:
                print("Felaktig inmatning. Välj siffror.")
                return
        else:
            chosen_genres = []

        rating_input = input("Minsta betyg (1–10, tryck Enter för standard 6.5): ").strip()
        try:
            rating = float(rating_input) if rating_input else 6.5
        except ValueError:
            rating = 6.5

        movie_data = self.api.get_random_movie(genre=chosen_genres, vote_average_gte=rating)
        if not isinstance(movie_data, dict):
            print(movie_data)
            return

        movie = Movie(
            title=movie_data.get("title", "Okänd titel"),
            genre=movie_data.get("genre", "Okänd genre"),
            rating=movie_data.get("rating", 0.0),
            year=int(str(movie_data.get("release_date", "0"))[:4]) if movie_data.get("release_date") else 0,
            plot=movie_data.get("plot", "Ingen beskrivning tillgänglig.")
        )

        movie.show_info()
        self.ask_save(movie)

    def ask_save(self, movie):
        choice = input("\nVill du spara filmen i favoriter? (j/n): ").lower().strip()
        if choice == "j":
            self.fav_manager.save_favorites(movie.to_dict())
            print(f"Filmen '{movie.title}' har sparats i favoriter.")

    def show_favorites(self):
        favorites = self.fav_manager.show_favorites()
        movie_objects = [Movie.from_dict(f) for f in favorites]
        Movie.show_favorites(movie_objects)

    def edit_favorites(self):
        self.fav_manager.edit_favorites()


if __name__ == "__main__":
    app = App()
    app.run()
 