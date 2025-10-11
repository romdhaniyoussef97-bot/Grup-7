from datetime import datetime

class Movie:
    def __init__(self, title: str, genre: str, rating: float, year: int, plot: str = "Okänd plot"):
        self.title = title
        self.genre = genre
        self.rating = rating
        self.year = year
        self.plot = plot

    def show_info(self):
        genre = ", ".join(self.genre) if isinstance(self.genre, list) else self.genre

        if self.rating >= 7.0:
            status = "Populär"
        elif self.rating >= 5.0:
            status = "En bra film"
        else: 
            status = "Kan vara bra eller dålig"

        current_year = datetime.now().year
        age = current_year - self.year

        print(f"\n{self.title} ({self.year}) - IMBb: {self.rating} {status} {self.plot}")
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

        formatted_favorites = []

        if favorites:
            for i, movie in enumerate(favorites, start=1):
                title = getattr(movie, 'title', movie.get("title", "Okänd titel"))
                year = getattr(movie, 'year', movie.get("year", "Okänd år"))
                genre = getattr(movie, 'genre', movie.get("genre", "Okänd genre"))
                rating = getattr(movie, 'rating', movie.get("rating", "Okänd rating"))

                if isinstance(genre, list):
                    genre = ", ".join(genre)
                
                formatted_favorites.append(
                    f"{i}. 🎥{title} {year} |  🎭 {genre} | ⭐ {rating}"
                )
        else:
            formatted_favorites.append("Du har inga favoriter än.")
        
        return formatted_favorites
       