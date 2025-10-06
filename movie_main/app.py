from api.tmdb_api import TMDB_API
from models.movie_model import Movie
from storage.repo import save_favorite, load_favorites
from prettytable import PrettyTable

class App:
    def __init__(self):
        self.api = TMDB_API()
        self.running = True

    def run(self):
        """Main loop that keeps the app running until user exits."""
        while self.running:
            print("\n Welcome to Movie Recommender+")
            print("1. Search movie by title")
            print("2. Discover by genre & rating")
            print("3. Get random movie")
            print("4. Show favorites")
            print("0. Exit")

            choice = input("\nSelect an option: ").strip()

            if choice == "1":
                self.search_movie_flow()
            elif choice == "2":
                self.genre_discover_flow()
            elif choice == "3":
                self.random_movie_flow()
            elif choice == "4":
                self.show_favorites()
            elif choice == "0":
                print("👋 Goodbye!")
                self.running = False
            else:
                print("Invalid choice. Try again.")

    # --- Option 1: Search movie by title ---
    def search_movie_flow(self):
        title = input("\nEnter movie title: ").strip()
        results = self.api.search_movie(title)
        if not results:
            print("❌ No movies found.")
            return

        table = PrettyTable(["#", "Title", "Year", "Rating"])
        for i, m in enumerate(results, start=1):
            table.add_row([i, m.get("title"), m.get("release_date", "")[:4], m.get("vote_average")])
        print(table)

        try:
            choice = int(input("Select a movie number to view details (0 to cancel): "))
            if choice == 0:
                return
            selected = results[choice - 1]
        except (ValueError, IndexError):
            print("❌ Invalid selection.")
            return

        movie = Movie(
            title=selected.get("title"),
            year=selected.get("release_date", "")[:4],
            genre="N/A",
            rating=selected.get("vote_average"),
            plot=selected.get("overview", "No description.")
        )

        self.display_movie(movie)
        self.ask_save(movie)

    # --- Option 2: Discover by genre & rating ---
    def genre_discover_flow(self):
        genres = self.api.get_genres()
        print("\nAvailable Genres:")
        for g in genres:
            print("-", g)

        chosen = input("\nEnter one or more genres (separated by spaces): ").strip()
        rating = input("Minimum rating (1–10, press Enter to skip): ").strip()
        rating = float(rating) if rating else None

        movie = self.api.get_random_movie(genre=chosen, vote_average_gte=rating)
        if not movie:
            print("❌ Could not find a movie with those filters.")
            return

        movie_obj = Movie(**movie)
        self.display_movie(movie_obj)
        self.ask_save(movie_obj)

    # --- Option 3: Random movie ---
    def random_movie_flow(self):
        movie = self.api.get_random_movie()
        if not movie:
            print("❌ No movie found.")
            return

        m = Movie(**movie)
        self.display_movie(m)
        self.ask_save(m)

    # --- Option 4: Show favorites ---
    def show_favorites(self):
        favorites = load_favorites()
        if not favorites:
            print("\nNo saved favorites yet.")
            return

        table = PrettyTable(["Title", "Year", "Rating"])
        for f in favorites:
            table.add_row([f.get("title"), f.get("year"), f.get("rating")])
        print(table)

    # --- Helper functions ---
    def ask_save(self, movie):
        choice = input("Save to favorites? (y/n): ").lower().strip()
        if choice == "y":
            save_favorite(movie.__dict__)
            print("✅ Movie saved to favorites!")

    def display_movie(self, movie):
        print(f"\n {movie.title} ({movie.year})")
        print(f"Genre: {movie.genre}")
        print(f"Rating: {movie.rating}")
        print(f"Plot: {movie.plot}")

# --- Entry point for testing ---
if __name__ == "__main__":
    app = App()
    app.run()
