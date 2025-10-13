🎬 Movie Recommender

Movie Recommender är ett Python-program som genererar slumpmässiga filmtips baserat på användarens val av genre och betyg.
Filmerna hämtas i realtid från The Movie Database (TMDB) via deras API.
Användaren kan även spara sina favoritfilmer lokalt i en JSON-fil.

🚀 Funktioner

Välj en eller flera genrer

Ange minimibetyg (1–10)

Generera slumpmässig film via TMDB API

Spara och visa favoritfilmer

Ta bort enstaka eller alla favoriter

⚙️ Installation och körning
1️⃣ Klona projektet
git clone https://github.com/romdhaniyoussef97-bot/Grup-7.git
cd Grup-7

2️⃣ Skapa en virtuell miljö (rekommenderas)
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3️⃣ Installera beroenden
pip install -r requirements.txt

🔑 TMDB API – .env-fil

För att programmet ska fungera behöver du skapa en .env-fil i projektets rotmapp.
Den används för att lagra din TMDB API-nyckel.

Gör så här:

Skapa en fil i projektets rotmapp som heter .env

Klistra in följande rad:

API_KEY=HÄR SKA DET VARA EN API-NYCKEL


Spara filen

💡 Du kan skapa en egen nyckel via:
https://www.themoviedb.org/settings/api

▶️ Kör programmet

Starta programmet genom att köra:

python movie_main/app.py

📚 Använda bibliotek

Externa bibliotek

Bibliotek	Syfte
requests	Hämtar data från TMDB API
python-dotenv	Läser in miljövariabler (API-nyckeln) från .env
random	Slumpar filmer och sidor i API-svaren
json	Sparar och läser favoritfilmer till/från JSON
pathlib	Hanterar filvägar på ett OS-oberoende sätt

Standardbibliotek
Bibliotek	Syfte
os	Filvägar och miljöhantering
typing	Typannoteringar (valfritt)

👥 Team och ansvar
Namn	Modul	Ansvar
Fredrik	api/tmdb_api.py	Hanterar kommunikation med TMDB API och generering av filmdata
Nick	storage/repo.py	Lagring till JSON – sparar, raderar och hanterar favoriter
Youssef	app.py	Användargränssnitt (UI) – meny, val och utskrifter
Andy	models/movie_model.py	Klass för filmobjekt – struktur, attribut och metoder
🧠 Övrig information

API: The Movie Database (TMDB)

Lagring sker lokalt i data/favorites.json

Programmet körs i terminalen

Kräver Python 3.9 eller senare
