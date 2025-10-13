from api.tmdb_api import TMDB_API
from models.movie_model import Movie
from storage.repo import FavoritesManager


class App:
    def __init__(self):
        self.api = TMDB_API()
        self.fav_manager = FavoritesManager("data/favorites.json")
        self.running = True

    def run(self):
        """Main loop that keeps the app running until user exits."""
        while self.running:
            print("\n=== MOVIE RECOMMENDER+ ===")
            print("1. Slumpmässig film (välj genre och/eller betyg)")
            print("2. Visa favoriter")
            print("3. Hantera favoriter")
            print("0. Avsluta")

            choice = input("\nVälj ett alternativ: ").strip()

            if choice == "1":
                self.random_movie_flow()
            elif choice == "2":
                self.show_favorites()
            elif choice == "3":
                self.edit_favorites_flow()
            elif choice == "0":
                print("Programmet avslutas.")
                self.running = False
            else:
                print("Ogiltigt val. Försök igen.")

    # --- Option 1: Random movie ---
    def random_movie_flow(self):
        genres = self.api.get_genres()
        print("\nTillgängliga genrer:")
        for i, g in enumerate(genres, start=1):
            print(f"{i}. {g}")

        chosen_numbers = input("\nAnge genrenumren (separera med mellanslag) eller tryck Enter för slumpmässig film: ").strip()
        chosen_genres = []

        if chosen_numbers:
            try:
                chosen_indices = [int(num) - 1 for num in chosen_numbers.split()]
                chosen_genres = [genres[i] for i in chosen_indices if 0 <= i < len(genres)]
            except ValueError:
                print("Fel format. Välj nummer med mellanslag, t.ex. 1 3 5.")
                return

        rating = input("Ange minsta betyg (1–10, tryck Enter för standard 6.5): ").strip()
        rating = float(rating) if rating else 6.5

        movie_data = self.api.get_random_movie(genre=" ".join(chosen_genres), vote_average_gte=rating)
        if not movie_data or "title" not in movie_data:
            print("Kunde inte hämta film.")
            return

        try:
            year = int(movie_data.get("releas_date", "0000")[:4])
        except ValueError:
            year = 0

        movie = Movie(
            title=movie_data.get("title", "Okänd titel"),
            genre=chosen_genres if chosen_genres else "Okänd genre",
            rating=float(movie_data.get("rating", 0)),
            year=year,
            plot=movie_data.get("plot", "Okänd handling.")
        )

        print(movie.show_info())
        self.ask_save(movie)

    # --- Option 2: Show favorites ---
    def show_favorites(self):
        favorites = self.fav_manager.get_favorites()
        formatted_list = Movie.show_favorites([Movie.from_dict(f) for f in favorites])
        print("\n".join(formatted_list))

    # --- Option 3: Edit favorites ---
    def edit_favorites_flow(self):
        print("\n1. Ta bort specifik film")
        print("2. Töm hela listan")
        print("0. Tillbaka")
        choice = input("\nVälj ett alternativ: ").strip()

        if choice == "1":
            favorites = self.fav_manager.get_favorites()
            if not favorites:
                print("Inga favoriter att ta bort.")
                return

            for i, movie in enumerate(favorites, start=1):
                print(f"{i}. {movie.get('title', 'Okänd titel')}")

            try:
                index = int(input("\nAnge numret på filmen du vill ta bort: ").strip())
                result = self.fav_manager.remove_favorite(index)
                print(result["message"] if "message" in result else "Filmen har tagits bort.")
            except ValueError:
                print("Ogiltigt val.")
        elif choice == "2":
            confirm = input("Är du säker på att du vill ta bort alla favoriter? (y/n): ").lower().strip()
            if confirm == "y":
                result = self.fav_manager.clear_favorites()
                print(result["message"])
        elif choice == "0":
            return
        else:
            print("Ogiltigt val.")

    # --- Helper: Save favorite ---
    def ask_save(self, movie):
        choice = input("\nVill du spara filmen i favoriter? (y/n): ").lower().strip()
        if choice == "y":
            result = self.fav_manager.save_favorites(movie)
            print(result["message"])
