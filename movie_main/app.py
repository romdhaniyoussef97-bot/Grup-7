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

        self.display_movie(movie)
        self.ask_save(movie)

    def ask_save(self, movie):
        choice = input("\nVill du spara filmen i favoriter? (j/n): ").lower().strip()
        if choice == "j":
            self.fav_manager.save_favorites(movie)
            print(f"Filmen '{movie.title}' har sparats i favoriter.")

    def show_favorites(self):
        favorites = self.fav_manager.show_favorites()
        if not favorites:
            print("\nDu har inga favoriter ännu.")
            return

        print("\n=== DINA FAVORITFILMER ===")
        for i, data in enumerate(favorites, start=1):
            title = data.get("title", "Okänd titel")
            genre = data.get("genre", "Okänd genre")
            rating = data.get("rating", "N/A")
            year = data.get("year", "Okänt år")
            plot = data.get("plot", "")
            print(f"\n{i}. {title} ({year})")
            print(f"   Genre: {genre}")
            print(f"   Betyg: {rating}")
            print(f"   {plot[:120]}...")

    def edit_favorites(self):
        favorites = self.fav_manager.show_favorites()
        if not favorites:
            print("\nDet finns inga filmer att redigera.")
            return

        print("\n=== REDIGERA FAVORITER ===")
        for i, film in enumerate(favorites, start=1):
            print(f"{i}. {film.get('title', 'Okänd titel')}")

        choice = input("Ange numret på filmen du vill ta bort (eller 'a' för att ta bort alla): ").strip().lower()

        if choice == 'a':
            favorites = []
            print("Alla favoriter har tagits bort.")
        else:
            try:
                index = int(choice) - 1
                if 0 <= index < len(favorites):
                    removed = favorites.pop(index)
                    print(f"Filmen '{removed.get('title', 'Okänd titel')}' har tagits bort.")
                else:
                    print("Ogiltigt val.")
            except ValueError:
                print("Felaktig inmatning.")

        import json
        with open(self.fav_manager.filename, "w", encoding="utf-8") as f:
            json.dump(favorites, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    app = App()
    app.run()
