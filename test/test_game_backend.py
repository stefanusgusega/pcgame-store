import pytest
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from game_backend import GameDatabase

@pytest.fixture
def gameDB():
    db = GameDatabase("../games.txt")
    return db

def test_get_user(gameDB):
    assert gameDB.get_user("img/game1.jpg") == ("Tomb Raider","1.99 GB","235000","Tomb Raider","Windows 8","2 Ghz","DirectX9","5 GB","https://pcgamestore/download/o5Sub0776m")

