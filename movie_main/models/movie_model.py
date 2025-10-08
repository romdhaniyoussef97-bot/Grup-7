from datetime import datetime

class Movie:
    def __init__(self, title: str, genre: str, rating: float, year: int):
        self.title = title
        self.genre = genre
        self.rating = rating
        self.year = year

    def show_info(self):
        if self.rating >= 7.0:
            status = "Populär"
        elif self.rating >= 5.0:
            status = "En bra film"
        else: 
            status = "Kan vara bra eller dålig"

        current_year = datetime.now().year
        age = current_year - self.year

        print(f"\n{self.title} ({self.year}) - IMBD: {self.rating} {status} {self.year}")
        print(f"\n filmen är {age} år gammal")
    
    def to_dict(self):
        return{
            "title": self.title,
            "genre": self.genre,
            "rating": self.rating,
            "year": self.year
        }
    
    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            data.get("title", "Okänd titel"),
            data.get("genre", "Okänd genre"),
            float(data.get("rating", 0.0)),
            int(data.get("year", 0))
        )