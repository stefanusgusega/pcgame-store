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

class LoginUserWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def login(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            program.current = "main_page"
        else:
            invalidForm()

    def register(self):
        self.reset()
        program.current = "register"

    def reset(self):
        self.email.text = ""
        self.password.text = ""