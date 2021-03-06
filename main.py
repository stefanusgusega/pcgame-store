from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.core.text import LabelBase

from backend.user_backend import UserDatabase
from backend.ewallet_backend import EwalletDatabase
from backend.game_backend import GameDatabase

from utils import generate_string
from constant import LOGIN_PAGE, REGISTER_PAGE, MAIN_PAGE, PURCHASE_PAGE, DOWNLOAD_PAGE,GAME_PAGE, FIRST_PAGE,PROFILE_PAGE,HELP_PAGE,TOPUP_PAGE,FORGOT_PAGE,CHANGE_PAGE


LabelBase.register(name="Helvetica",
    fn_regular="asset/font/Helvetica 400.ttf",
    fn_bold="asset/font/helvetica-bold.ttf"
    )
LabelBase.register(name="Circular",
    fn_regular="asset/font/lineto-circular-pro-medium.ttf",
    fn_bold="asset/font/lineto-circular-black.ttf"
    )


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
    balance = ObjectProperty(None)

    def register(self):
        if self.full_name.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0 and self.email.text.count('!') == 0 and self.password.text != "" and self.nationality.text != '' and self.phonenumber.text != '':
            if(db.add_user(self.email.text, self.password.text, self.full_name.text, self.dateofbirth.text, self.nationality.text, self.phonenumber.text)==1):
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


class LoginUserWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def login(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            program.current = MAIN_PAGE
        else:
            invalidLogin()

    def register(self):
        self.reset()
        program.current = REGISTER_PAGE

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class DownloadWindow(Screen):

    def download(self):
        pop = Popup(title='Download game',
                  content=Label(text='ini linknya'),
                  size_hint=(None, None), size=(500, 200))
        pop.open()


class MainWindow(Screen):
    balance = ObjectProperty(None)
    search = ObjectProperty(None)
    action = ObjectProperty(None)
    romance = ObjectProperty(None)
    comedy = ObjectProperty(None)
    current = ""

    def logout(self):
        program.current = LOGIN_PAGE
    def showdetails(self, picture):
        GameDetailsWindow.picturename = picture

    def on_enter(self, *args):
        password, full_name, dateofbirth, nationality, phonenumber, created = db.get_user(self.current)
        balanced = db1.get_balance(self.current)
        self.balance.text = "Rp " + str(balanced)


class PurchaseWindow(Screen):

    balance = ObjectProperty(None)
    price = ObjectProperty(None)
    download = ObjectProperty(None)
    balanced = None
    priced = None
    def on_enter(self, *args):
        password, full_name, dateofbirth, nationality, phonenumber, created = db.get_user(MainWindow.current)
        balanced = db1.get_balance(MainWindow.current)
        name, size1, price1, description1, os1, processor1, graphics1, storage1,link = db2.get_user(GameDetailsWindow.picturename)
        priced = price1
        self.balance.text = balanced
        self.price.text = priced 
        self.download.text = "Buy " + name + " Confirmation"
        self.balanced = int(balanced)
        self.priced = int(priced)

    def purchase(self):
        
        
        if(int(self.balanced)>int(self.priced)):
            if(db1.substract_balance(MainWindow.current,self.priced)==1):
                self.reset()
                program.current = DOWNLOAD_PAGE
        else:
            invalidPurchase()
            program.current = PURCHASE_PAGE
            
            
    # def change(self):
    #     #POKOKNYA DISINI VALIDATE DULU YEEEE
    #     if(newpassword.text == newpassword1.text and MainWindow.current == self.email.text):
    #         db.change_passsword(email, newpassword)
    #         pop = Popup(title='Change Password',
    #                 content=Label(text='Your password is succesfully changed'),
    #                 size_hint=(None,None),size=(600,300),pos_hint={'x': 0.35, 'top':0.6})
    #         pop.open()
        
    def reset(self):
        self.balance.text = ""
        self.price.text = ""


class GameDetailsWindow(Screen):
    gambar = ObjectProperty(None)
    nama = ObjectProperty(None)
    ukuran = ObjectProperty(None)
    price = ObjectProperty(None)
    description = ObjectProperty(None)
    os = ObjectProperty(None)
    processor = ObjectProperty(None)
    graphics = ObjectProperty(None)
    storage = ObjectProperty(None)

    picturename = ""
    def on_enter(self, *args):
        name, size1, price1, description1, os1, processor1, graphics1, storage1,link = db2.get_user(self.picturename)
        self.gambar.source = self.picturename
        self.nama.text = name
        self.ukuran.text = "Size: " + size1
        self.description.text = "Description: " + description1
        self.price.text = "Price: " + price1
        self.os.text = "OS: " + os1
        self.processor.text = "Processor: " + processor1
        self.graphics.text = "Graphics: " + graphics1
        self.storage.text = "Storage: " + storage1
    
    def reset(self):
        pass
        self.nama.text = "<JUDUL GAME>" 
        self.size.text = "Size: "
        self.description.text = "Description: " 
        self.price.text = "Price: " 
        self.os.text = "OS: "
        self.processor.text = "Processor: "
        self.graphics.text = "Graphics: " 
        self.storage.text = "Storage: "

    

class ProfileWindow(Screen):
    full_name = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    balance = ObjectProperty(None)
    date_of_birth = ObjectProperty(None)
    nationality = ObjectProperty(None)
    phone_number = ObjectProperty(None)

    def on_enter(self, *args):
        password, full_name, date_of_birth, nationality, phone_number, created = db.get_user(MainWindow.current)
        balance = db1.get_balance(MainWindow.current)
        self.full_name_content.text = full_name
        self.email_content.text = MainWindow.current
        self.created_content.text = created
        self.balance_content.text = balance
        self.dob_content.text = date_of_birth
        self.nationality_content.text = nationality
        self.phone_number_content.text = phone_number


class HelpWindow(Screen):
    pass


class TopUpWindow(Screen):
    pass


class ForgotPasswordWindow(Screen):
    email = ObjectProperty(None)
    token = generate_string(8)
    written_token = ObjectProperty(None)

    def change(self):
        if db.get_user(self.email.text) != -1:
            try:
                db.send_email(self.email.text, self.token)
                pop = Popup(title='Email sent!',
                        content=Label(text='We have send you an email.\nCheck your inbox and enter the input the token above!'),
                        size_hint=(None,None),size=(600,300),pos_hint={'x': 1 / Window.width, 'y': 1 / Window.height })
                pop.open()
            except:
                pop = Popup(title='Email error!',
                    content=Label(text='We fail to send you email.\nRe-check your input or contact our staff'),
                    size_hint=(None,None),size=(600,300),pos_hint={'x': 1 / Window.width, 'y': 1 / Window.height })
                pop.open()
        else:
            pop = Popup(title='Email doesn\'t exist',
                    content=Label(text='You have not have an account at PCGame Store.\nYou should consider signing up!'),
                    size_hint=(None,None),size=(600,300),pos_hint={'x': 1 / Window.width, 'y': 1 / Window.height })
            pop.open()

    def validate(self):
        if(self.token == self.written_token.text):
            program.current = CHANGE_PAGE
            MainWindow.current = self.email.text


class ChangePasswordWindow(Screen):
    # oldpassword = ObjectProperty(None)
    email = ObjectProperty(None)
    newpassword = ObjectProperty(None)
    newpassword1 = ObjectProperty(None)
    def change(self):
        #POKOKNYA DISINI VALIDATE DULU YEEEE
        if(self.newpassword.text == self.newpassword1.text and MainWindow.current == self.email.text):
            db.change_password(self.email.text, self.newpassword.text)
            pop = Popup(title='Change Password',
                    content=Label(text='Your password is succesfully changed'),
                    size_hint=(None,None),size=(600,300),pos_hint={'x': 0.35, 'top':0.6})
            pop.open()


class DownloadWindow(Screen):

    def download(self):
        name, size1, price1, description1, os1, processor1, graphics1, storage1,link = db2.get_user(GameDetailsWindow.picturename)
        pop = Popup(title='Download game',
                  content=Label(text=link),
                  size_hint=(0.6,None),size=(600,300),pos_hint={'x': 0.25, 'top':0.6})
        
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

db = UserDatabase("database/users.txt")
db1 = EwalletDatabase("database/ewallet.txt")
db2 = GameDatabase("database/games.txt")

screens = [
    LoginUserWindow(name=LOGIN_PAGE), RegisterUserWindow(name=REGISTER_PAGE), 
    MainWindow(name=MAIN_PAGE),PurchaseWindow(name=PURCHASE_PAGE),
    DownloadWindow(name=DOWNLOAD_PAGE),GameDetailsWindow(name=GAME_PAGE),
    FirstWindow(name=FIRST_PAGE),ProfileWindow(name=PROFILE_PAGE),HelpWindow(name=HELP_PAGE),
    TopUpWindow(name=TOPUP_PAGE),ForgotPasswordWindow(name=FORGOT_PAGE),ChangePasswordWindow(name=CHANGE_PAGE)
]

for screen in screens:
    program.add_widget(screen)

program.current = FIRST_PAGE

if __name__ == "__main__":
    MyMainApp().run()
