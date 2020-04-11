from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image
from backend import Database
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox

from variable import *
from invalidCheck import *

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