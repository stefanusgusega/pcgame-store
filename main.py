from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from backend import Database


class RegisterUserWindow(Screen):
    full_name = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def register(self):
        if self.full_name.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0 and self.email.text.count('!') == 0 and self.password.text != "":
            db.add_user(self.email.text, self.password.text, self.full_name.text)
            MainWindow.current = self.email.text
            self.reset()
            program.current = "main"
        else:
            invalidForm()

    def login(self):
        self.reset()
        program.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.full_name.text = ""


class LoginUserWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def login(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            program.current = "main"
        else:
            invalidLogin()

    def register(self):
        self.reset()
        program.current = "register"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class MainWindow(Screen):
    full_name = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logout(self):
        program.current = "login"

    def on_enter(self, *args):
        password, full_name, created = db.get_user(self.current)
        self.full_name.text = "Account Name: " + full_name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created


class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


kv = Builder.load_file("my.kv")
program = WindowManager()
db = Database("users.txt")

screens = [LoginUserWindow(name="login"), RegisterUserWindow(name="register"), MainWindow(name="main")]
for screen in screens:
    program.add_widget(screen)

program.current = "login"


class MyMainApp(App):
    def build(self):
        return program


if __name__ == "__main__":
    MyMainApp().run()
