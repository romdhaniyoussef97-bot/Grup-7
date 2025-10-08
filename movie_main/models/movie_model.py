from datetime import datetime

class Movie:
    def __init__(self, title: str, genre: str, rating: float, year: int, plot: str):
        self.title = title
        self.genre = genre
        self.rating = rating
        self.year = year
        self.plot = plot

    def show_info(self):
        if self.rating >= 7.0:
            status = "Populär"
        elif self.rating >= 5.0:
            status = "En bra film"
        else: 
            status = "Kan vara bra eller dålig"

        current_year = datetime.now().year
        age = current_year - self.year

        print(f"\n{self.title} ({self.year}) - IMBD: {self.rating} {status} {self.year} {self.plot}")
        print(f"\n filmen är {age} år gammal")
    
    def to_dict(self):
        return{
            "title": self.title,
            "genre": self.genre,
            "rating": self.rating,
            "year": self.year,
            "plot": self.plot
        }
    
    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            data.get("title", "Okänd titel"),
            data.get("genre", "Okänd genre"),
            float(data.get("rating", 0.0)),
            int(data.get("year", 0)),
            data.get("plot", "Okänd plot")
        )

    @staticmethod
    def show_favorites(favorites):
        print("\n" + "=" * 50)
        print("💖 DINA FAVORITFILMER 💖".center(50))
        print("=" * 50)

        if favorites:
            for i, movie in enumerate(favorites, start=1):
                print(f"\n{i}. 🎥 {movie.title} ({movie.year})")
                print(f"   🎭 Genre: {movie.genre}")
                print(f"   ⭐ Betyg: {movie.rating}")
            print("\n Totalt antal favoriter", len(favorites))
        else:
            print("Du har inga favoritfilmern ännu.")
        
        print("=" * 50)