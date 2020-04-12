from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from backend import Database
from constant import LOGIN_PAGE

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