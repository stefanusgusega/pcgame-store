from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image
from backend import Database
from kivy.uix.button import ButtonBehavior
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox
from constant import LOGIN_PAGE, REGISTER_PAGE, MAIN_PAGE, PURCHASE_PAGE, DOWNLOAD_PAGE,GAME_PAGE, FIRST_PAGE,PROFILE_PAGE,HELP_PAGE,TOPUP_PAGE

from util import invalidLogin, invalidForm, invalidPurchase

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
            program.current = "purchase"
        else:
            self.reset()
            program.current = "download"
        
    def reset(self):
        self.balance.text = ""
        self.price.text = ""