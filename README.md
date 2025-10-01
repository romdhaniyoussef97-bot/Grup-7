# Grup-7
Jensen AI dev. 
# Grup-7 · Movie Recommender

Console app that lets you search movies, filter by genre & rating, read community sentiment from reviews, and save favorites.

## Features
- 🔎 Search movies by title
- 🏷️ Browse by genre/category
- ⭐ Filter by rating (vote average & minimum vote count)
- 💬 Pull reviews and show quick sentiment (VADER)
- 💾 Save/remove favorites (JSON; switchable to SQLite)
- 🔁 Get related recommendations

## Tech Stack
- Python 3.11+
- `requests`, `python-dotenv`, `vaderSentiment`, `prettytable`
- Optional: `praw` (Reddit) or TMDb reviews

Project structure
movie-recommender/
│
├─ api/
│  ├─ __init__.py
│  ├─ omdb_api.py          # talk to OMDb
│  └─ reddit_api.py        # get Reddit comments (optional if no creds)
│
├─ models/
│  ├─ __init__.py
│  └─ movie_model.py       # Movie dataclass + helpers
│
├─ services/
│  ├─ __init__.py
│  └─ sentiment_service.py # VADER sentiment scoring
│
├─ storage/
│  ├─ __init__.py
│  └─ repo.py              # JSON or SQLite persistence
│
├─ config/
│  ├─ __init__.py
│  └─ settings.py          # reads API keys from .env
│
├─ data/
│  ├─ favorites.json
│  └─ cache.json           # (optional) store last queries
│
├─ app.py                  # menu / CLI UI
├─ main.py                 # entry point
├─ requirements.txt
└─ .env.example            # where to put keys


