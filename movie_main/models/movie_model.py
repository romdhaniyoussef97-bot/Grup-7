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

        return (f"🎥 {self.title} ({self.year})\n"
                f"   Genrer: {genre}\n"
                f"   Betyg: {self.rating} - {status}\n"
                f"   Ålder: {age} år\n"
                f"   Handling: {self.plot}\n")

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

        if not favorites:
            formatted_favorites.append("Du har inga favoriter än.")
            return formatted_favorites

        for i, movie in enumerate(favorites, start=1):
         if isinstance(movie, dict):
            title = movie.get("title", "Okänd titel")
            year = movie.get("year", "Okänd år")
            genre = movie.get("genre", "Okänd genre")
            rating = movie.get("rating", "Okänd rating")

        else:
            title = getattr(movie, "title", ("title", "Okänd titel"))
            year = getattr(movie, 'year',("year", "Okänd år"))
            genre = getattr(movie, 'genre',("genre", "Okänd genre"))
            rating = getattr(movie, 'rating',("rating", "Okänd rating"))

        if isinstance(genre, list):
                genre = ", ".join(genre)
                
        formatted_favorites.append(
            f"{i}. 🎥{title} {year} |  🎭 {genre} | ⭐ {rating}"
        )
    
        
        return formatted_favorites
       