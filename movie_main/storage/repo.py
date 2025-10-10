import json
import os

#En klass som behållare för all funktionalitet kring favoriter.
#Tre metoder för att spara, läsa och radera favoriter-listan i json.

class FavoritesManager:
    def __init__(self, filename):
        self.filename = filename

    def save_favorites(self, movie):
        if not os.path.exists(self.filename):    #Om filen inte finns, gör lista
            favorites = []
        
        else:
            try:
                with open(self.filename, "r", encoding="utf-8") as f: #Om filen finns, läs vad som finns i den och lägg till i favorites
                    favorites = json.load(f)
            except json.JSONDecodeError:
                favorites = []
        
        favorites.append(movie.to_dict()) #lägg filmen i listan
    
        with open(self.filename, "w", encoding="utf-8") as f:    # Öppna .json igen och skriv nya listan i filen.
            json.dump(favorites, f, indent=4, ensure_ascii=False)


    def show_favorites(self):

        if not os.path.exists(self.filename):
            return []  # Returnera tom lista om filen inte finns

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                favorites = json.load(f)
                return favorites if favorites else []  # Tom fil
            
        except json.JSONDecodeError:
            return []

#Till ANDY:

#manager = FavoritesManager('data/favorites.json')

#favorites = manager.show_favorites()
     

def edit_favorites(self):
        
    if not os.path.exists(self.filename):
        return []  # Returnera tom lista om filen inte finns

    try:
        with open(self.filename, "r", encoding="utf-8") as f:
            favorites = json.load(f)
            return favorites if favorites else []  # Tom fil
            
        except json.JSONDecodeError:
            return []

        numbered_list = [(i, film["title"]) for i, film in enumerate(favorites, start=1)]
        return numbered_list

    
    # 4️⃣ Decide on parameters:
        # remove_index → which movie to delete (passed in by UI)
        # clear_all → delete all movies (passed in by UI)
    
    # 5️⃣ Apply deletion:
        # If clear_all: favorites = []
        # If remove_index: delete the correct movie (careful with 0-based index)
    
    # 6️⃣ Save updated list back to JSON
    
    # 7️⃣ Return updated list or status message (so UI can show feedback)