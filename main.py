# main.py

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
from kivy.uix.gridlayout import GridLayout
from constant import LOGIN_PAGE, REGISTER_PAGE, MAIN_PAGE, PURCHASE_PAGE, DOWNLOAD_PAGE,GAME_PAGE, FIRST_PAGE,PROFILE_PAGE,HELP_PAGE,TOPUP_PAGE,FORGOT_PAGE,CHANGE_PAGE


class ImageButton(ButtonBehavior,Image):
    pass
class LabelButton(ButtonBehavior,Label):
    pass

class FirstWindow(Screen):
    pass

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
            program.current = "main_page"
        else:
            invalidForm()

    def login(self):
        self.reset()
        program.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.full_name.text = ""
        self.dateofbirth.text= ""
        self.nationality.text = ""
        self.phonenumber.text = ""


class LoginUserWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def login(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            program.current = "main_page"
        else:
            invalidLogin()

    def register(self):
        self.reset()
        program.current = "register"

    def reset(self):
        self.email.text = ""
        self.password.text = ""

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
            program.current = "purchase"
        else:
            self.reset()
            program.current = "download"
        
    def reset(self):
        self.balance.text = ""
        self.price.text = ""

class DownloadWindow(Screen):
    def download(self):
        pop = Popup(title='Download game',
                  content=Label(text='ini linknya'),
                  size_hint=(None, None), size=(500, 200))
        pop.open()


class MainWindow(Screen):
    full_name = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    balance = ObjectProperty(None)
    search = ObjectProperty(None)
    action = ObjectProperty(None)
    romance = ObjectProperty(None)
    comedy = ObjectProperty(None)
    current = ""

    def logout(self):
        program.current = "login"

    def on_enter(self, *args):
        password, full_name, created = db.get_user(self.current)
        self.full_name.text = "Account Name: " + full_name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created

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

class GameDetailsWindow(Screen):
    pass

class ProfileWindow(Screen):
    pass

class HelpWindow(Screen):
    pass
class TopUpWindow(Screen):
    pass
class ForgotPasswordWindow(Screen):
    def change(self):
        pop = Popup(title='Forgot Password',
                  content=Label(text='If we have your email on our database, \nwe will send you your new password.'),
                  size_hint=(None,None),size=(600,300),pos_hint={'x': 0.35, 'top':0.6})
        pop.open()
class ChangePasswordWindow(Screen):
    oldpassword = ObjectProperty(None)
    newpassword = ObjectProperty(None)
    newpassword1 = ObjectProperty(None)
    def change(self):
        #POKOKNYA DISINI VALIDATE DULU YEEEE
        pop = Popup(title='Change Password',
                  content=Label(text='Your password is succesfully changed'),
                  size_hint=(None,None),size=(600,300),pos_hint={'x': 0.35, 'top':0.6})
        pop.open()


class DownloadWindow(Screen):
    def download(self):
        pop = Popup(title='Download game',
                  content=Label(text='ini linknya'),
                  size_hint=(0.6,None),size=(600,300),pos_hint={'x': 0.35, 'top':0.6})
        pop.open()

class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None),size=(600,300),pos_hint={'x': 0.35, 'top':0.6})
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(625,300),pos_hint={'x': 0.35, 'top':0.6})

    pop.open()

def invalidPurchase():
    pop = Popup(title='Invalid Purchase', 
                    content = Label(text='Balance not enough to purchase game. \nPlease top up first'),
                    size_hint = (None,None), size=(600,300),pos_hint={'x': 0.35, 'top':0.6})
    pop.open()

class MyMainApp(App):
    def build(self):
        return program
kv = Builder.load_file("my.kv")
program = WindowManager()
db = Database("users.txt")

screens = [LoginUserWindow(name=LOGIN_PAGE), RegisterUserWindow(name=REGISTER_PAGE), 
MainWindow(name=MAIN_PAGE),PurchaseWindow(name=PURCHASE_PAGE),
DownloadWindow(name=DOWNLOAD_PAGE),GameDetailsWindow(name=GAME_PAGE),
FirstWindow(name=FIRST_PAGE),ProfileWindow(name=PROFILE_PAGE),HelpWindow(name=HELP_PAGE),
TopUpWindow(name=TOPUP_PAGE),ForgotPasswordWindow(name=FORGOT_PAGE),ChangePasswordWindow(name=CHANGE_PAGE)]
for screen in screens:
    program.add_widget(screen)

program.current = FIRST_PAGE




if __name__ == "__main__":
    MyMainApp().run()
