from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from backend import Database
from constant import PURCHASE_PAGE, DOWNLOAD_PAGE
from util import invalidPurchase

from WindowManager import WindowManager

program = WindowManager()
db = Database("users.txt")

class PurchaseWindow(Screen):

    saldo = ObjectProperty(None)
    harga = ObjectProperty(None)
    def on_enter(self, *args):
        self.balance.text = "80.000"
        self.price.text = "100.000"

    def purchase(self):
        harga = 80
        saldo = 100
        
        if(saldo<harga):
            invalidPurchase()
            program.current = PURCHASE_PAGE
        else:
            self.reset()
            program.current = DOWNLOAD_PAGE
        
    def reset(self):
        self.balance.text = ""
        self.price.text = ""