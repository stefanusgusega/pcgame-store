from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from backend import Database
from constant import LOGIN_PAGE, MAIN_PAGE
from util import invalidLogin, invalidForm

from WindowManager import WindowManager

program = WindowManager()
db = Database("users.txt")

class RegisterUserWindow(Screen):
    full_name = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    dateofbirth = ObjectProperty(None)
    nationality = ObjectProperty(None)
    phonenumber = ObjectProperty(None)

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
        self.dateofbirth.text= ""
        self.nationality.text = ""
        self.phonenumber.text = ""