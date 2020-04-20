import pytest
import os, sys, inspect

sys.path.insert(0, '..')

from backend.game_backend import GameDatabase


@pytest.fixture
def gameDB():
    db = GameDatabase("../database/games.txt")
    return db

def test_get_game(gameDB):
    assert gameDB.get_user("img/game1.jpg") != ("Jones Raider","213.99 GB","235000","Tomb Raider","Windows 8","2 Ghz","DirectX9","5 GB","https://pcgamestore/download/o5Sub0776m")

