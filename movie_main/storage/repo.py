import json

# En klass som behållare för all funktionalitet kring favoriter.
# Tre metoder: spara, läsa och radera favoriter-listan i JSON.

class FavoritesManager:
    def __init__(self, filename):
        self.filename = filename

    def save_favorites(self, movie):                        # Spara en film
        try:
                                                        # Om filen finns, läs vad som finns i den
            with open(self.filename, "r", encoding="utf-8") as f:
                favorites = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
                                                            # Om filen saknas eller är tom/ogiltig, skapa tom lista
            favorites = []

                                            # Kolla så att filmen inte redan finns i listan
        if not any(f["title"] == movie.title for f in favorites):
            favorites.append(movie.to_dict())  # Lägg filmen i listan


            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(favorites, f, indent=4, ensure_ascii=False) # Spara den nya listan i JSON-filen

            # Returnera bekräftelse till UI
            return {"success": True, "message": f"Filmen '{movie.title}' har sparats."}
        else:
            return {"success": False, "message": f"Filmen '{movie.title}' finns redan i favoriter."}

    # Funktion för att ta fram en lista med filmer ur JSON

    def get_favorites(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                favorites = json.load(f)

                # Returnera listan om det finns något i den, annars en tom lista
                return favorites if favorites else []
            
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    # Funktion för att radera en film ur JSON

    def remove_favorite(self, index_to_remove):  #index to remove användarens val från UI
       
        favorites = self.get_favorites()    # Hämtar listan med filmer
        if not favorites:                   # Om listan är tom
            return []

        # Kolla att användarens val finns i listans intervall

        if 0 <= index_to_remove < len(favorites):
            removed_movie = favorites.pop(index_to_remove)  # skapar variabel med borttagna filmen
        with open(self.filename, "w", encoding="utf-8") as f:
        # Spara uppdaterad lista utan vald film tillbaka till JSON
            json.dump(favorites, f, indent=4, ensure_ascii=False)

            return {"success": True, "Removed_movie": removed_movie}  # Returnera filmen som togs bort
        else:
            return {"success": False, "message": "Ogiltigt val. Ingen film raderades."}


    # Funktion för att radera alla favoriter i JSON
    def clear_favorites(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            favorites = []  # Skapa tom lista
            json.dump(favorites, f, indent=4, ensure_ascii=False)  # Skriv tom lista till filen
        return {"success": True, "message": "Alla favoriter har raderats."}

    
