import pytest
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from ewallet_backend import EwalletDatabase

@pytest.fixture
def eWalletDB():
    db = EwalletDatabase("../ewallet.txt")
    return db

def test_get_balance(eWalletDB):
    assert eWalletDB.get_balance("jones@gmail.com") != -1

def test_substract(eWalletDB):
    oldBalance = int(eWalletDB.get_balance("jones@gmail.com"))
    assert eWalletDB.substract_balance("jones@gmail.com",20) == 1
    assert int(eWalletDB.get_balance("jones@gmail.com")) == oldBalance-20