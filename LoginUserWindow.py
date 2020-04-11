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

class LoginUserWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def login(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            program.current = MAIN_PAGE
        else:
            invalidPurchase()

    def register(self):
        self.reset()
        program.current = REGISTER_PAGE

    def reset(self):
        self.email.text = ""
        self.password.text = ""