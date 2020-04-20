import pytest
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from user_backend import UserDatabase

@pytest.fixture
def userDB():
    db = UserDatabase("../users.txt")
    return db

def testEmail(userDB):
    assert userDB.validate("jones@gmail.com", "jon") == True

def test_get_user(userDB):
    assert userDB.get_user("jones@gmail.com") == ("jon","Jones NA","2000-01-01","Indonesia","009213847","2020-04-13")

def test_add_user(userDB):
    assert userDB.add_user("jones@gmail.com","jon","Jones NA","2000-01-01","Indonesia","009213847") == -1

def test_changePassword(userDB):
    assert userDB.change_password("jon@gmail.com","jon") == -1
    assert userDB.change_password("jones@gmail.com","jon") == 1
