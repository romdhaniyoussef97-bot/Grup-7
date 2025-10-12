import json

class FavoritesManager:
    def __init__(self, filename):
        self.filename = filename

    def save_favorites(self, movie):   

        try:                                           
            with open(self.filename, "r", encoding="utf-8") as f:
                favorites = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
                                                
            favorites = []

        if not any(f["title"] == movie.title for f in favorites):
            favorites.append(movie.to_dict())  

            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(favorites, f, indent=4, ensure_ascii=False) 

            return {"success": True, "message": f"Filmen '{movie.title}' har sparats."}
        else:
            return {"success": False, "message": f"Filmen '{movie.title}' finns redan i favoriter."}

    def get_favorites(self):

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                favorites = json.load(f)
                return favorites if favorites else []
            
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def remove_favorite(self, index_to_remove):
       
        favorites = self.get_favorites() 
        if not favorites:                   
            return {"success": False, "message": "Listan är tom."}
        
        index_to_remove -= 1

        if 0 <= index_to_remove < len(favorites):
            removed_movie = favorites.pop(index_to_remove)  
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(favorites, f, indent=4, ensure_ascii=False)

            return {"success": True, "Removed_movie": removed_movie}
        else:
            return {"success": False, "message": "Ogiltigt val. Ingen film raderades."}

    def clear_favorites(self):

        with open(self.filename, "w", encoding="utf-8") as f:
            favorites = []  
            json.dump(favorites, f, indent=4, ensure_ascii=False)  
        return {"success": True, "message": "Alla favoriter har raderats."}

    
