import pytest
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from user_backend import UserDatabase

@pytest.fixture
def userDB():
    db = UserDatabase("users.txt")
    return db

def testEmail(userDB):
    assert userDB.validate("jones@gmail.com", "jon") == True