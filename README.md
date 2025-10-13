# Movie Recommender

## Beskrivning
Movie Recommender är ett program som genererar slumpmässiga filmer baserat på genre och betyg som användaren väljer. Filmerna och all information hämtas från TMDB API.

## Installation och körning

1. **Kloning av repository**
```bash
git clone https://github.com/romdhaniyoussef97-bot/Grup-7.git
cd Grup-7
```

2. **Installera beroenden**
```bash
pip install -r requirements.txt
```

3. **Skapa en `.env`-fil i projektets root-mapp**  
   Lägg in din TMDB API-nyckel:
```
API_KEY=DIN_API_NYCKEL_HÄR
```

4. **Kör programmet**
```bash
python movie_main/UI/app.py
```

## Team och ansvarsområden

| Namn   | Modul / Ansvar |
|--------|----------------|
| Fredrik | `api/tmdb_api.py` – Hämtar data från TMDB API och hanterar API-förfrågningar |
| Nick    | `storage/repo.py` – Lagring i JSON, hantering av favoriter (läsa, spara, ta bort) |
| Youssef | `UI / app.py` – User interface, tar emot användarinput och visar data |
| Andy    | `models/movie_model.py` – Movie-klass för att skapa och hantera filmobjekt |

## Använda programmet
1. Starta programmet.  
2. Välj ett alternativ från menyn:  
   - Hämta slumpmässig film (med genreval)  
   - Visa favoriter  
   - Redigera favoriter  
   - Avsluta  

Favoriter sparas i en JSON-fil (`data/favorites.json`) och kan redigeras eller raderas via UI.

## Beroenden
- Python 3.9+  
- requests  
- python-dotenv  
- random  
- json  
- os  

