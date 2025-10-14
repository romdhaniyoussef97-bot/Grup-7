import sys
from pathlib import Path
import json
import pytest


sys.path.append(str(Path(__file__).resolve().parent.parent))

from storage.repo import FavoritesManager


class MockMovie:
    def __init__(self, title):
        self.title = title
    def to_dict(self):
        return {"title": self.title}
    
def test_save_favorites(tmp_path):
    filepath = tmp_path / "favorites.json"
    manager = FavoritesManager(filepath)
    movie = MockMovie("Babe: Den modige lilla grisen")

    result = manager.save_favorites(movie)

    assert result["success"] is True
    assert "sparats" in result["message"]

    with open(filepath, encoding="utf-8") as f:
        data = json.load(f)
    assert data == [{"title": "Babe: Den modige lilla grisen"}]

def test_save_duplicate_favorites(tmp_path):
    filepath = tmp_path / "favorites.json"
    manager = FavoritesManager(filepath)
    movie = MockMovie("Babe: Den modige lilla grisen")

    manager.save_favorites(movie)      # första gången
    result = manager.save_favorites(movie)  # andra gången

    assert result["success"] is False
    assert "finns redan" in result["message"]

    with open(filepath, encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == 1

def test_invalid_json(tmp_path):
    filepath = tmp_path / "favorites.json"
    filepath.write_text("{ not valid json")  # ogiltig JSON

    manager = FavoritesManager(filepath)
    movie = MockMovie("Jönssonligan")
    result = manager.save_favorites(movie)

    assert result["success"] is True

    with open(filepath, encoding="utf-8") as f:
        data = json.load(f)
    assert data == [{"title": "Jönssonligan"}]
