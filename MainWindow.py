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

class MainWindow(Screen):
    full_name = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    balance = ObjectProperty(None)
    current = ""

    def logout(self):
        program.current = LOGIN_PAGE

    def on_enter(self, *args):
        password, full_name, created = db.get_user(self.current)
        self.full_name.text = "Account Name: " + full_name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created