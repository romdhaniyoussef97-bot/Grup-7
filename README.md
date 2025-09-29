# Grup-7
Jensen AI dev. 
🎬 Movie Recommender+ (OMDb + Reddit Sentiment)
Core idea:
 You search a title → we fetch official info/ratings from OMDb → we also pull recent Reddit comments about that movie and run a quick sentiment analysis (how positive/negative people feel). You can save favorites and come back later.
 All console-based, clean output, modular, and GitHub-ready.

🧱 Project structure
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
