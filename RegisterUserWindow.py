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

class RegisterUserWindow(Screen):
    full_name = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def register(self):
        if self.full_name.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0 and self.email.text.count('!') == 0 and self.password.text != "":
            db.add_user(self.email.text, self.password.text, self.full_name.text)
            MainWindow.current = self.email.text
            self.reset()
            program.current = MAIN_PAGE
        else:
            invalidForm()

    def login(self):
        self.reset()
        program.current = LOGIN_PAGE

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.full_name.text = ""