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

class MainWindow(Screen):
    full_name = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logout(self):
        program.current = LOGIN_PAGE

    def on_enter(self, *args):
        password, full_name, created = db.get_user(self.current)
        self.full_name.text = "Account Name: " + full_name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created