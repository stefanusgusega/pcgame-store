from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from constant import REGISTER_PAGE, MAIN_PAGE
from backend import Database
from util import invalidForm

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
            program.current = MAIN_PAGE
        else:
            invalidForm()

    def register(self):
        self.reset()
        program.current = REGISTER_PAGE

    def reset(self):
        self.email.text = ""
        self.password.text = ""