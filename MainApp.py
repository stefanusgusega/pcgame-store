from kivy.app import App
from kivy.lang import Builder

from backend import Database
from constant import LOGIN_PAGE, REGISTER_PAGE, MAIN_PAGE, PURCHASE_PAGE, DOWNLOAD_PAGE,GAME_PAGE, FIRST_PAGE,PROFILE_PAGE,HELP_PAGE,TOPUP_PAGE
from util import invalidLogin, invalidForm, invalidPurchase

from ImageButton import ImageButton
from LabelButton import LabelButton
from FirstWindow import FirstWindow
from RegisterUserWindow import RegisterUserWindow
from LoginUserWindow import LoginUserWindow
from PurchaseWindow import PurchaseWindow
from DownloadWindow import DownloadWindow
from MainWindow import MainWindow
from GameDetailsWindow import GameDetailsWindow
from ProfileWindow import ProfileWindow
from HelpWindow import HelpWindow
from TopUpWindow import TopUpWindow
from WindowManager import WindowManager

kv = Builder.load_file("my.kv")
program = WindowManager()
db = Database("users.txt")

screens = [LoginUserWindow(name=LOGIN_PAGE), RegisterUserWindow(name=REGISTER_PAGE), MainWindow(name=MAIN_PAGE), PurchaseWindow(name=PURCHASE_PAGE), DownloadWindow(name=DOWNLOAD_PAGE), GameDetailsWindow(name=GAME_PAGE), FirstWindow(name=FIRST_PAGE), ProfileWindow(name=PROFILE_PAGE), HelpWindow(name=HELP_PAGE), TopUpWindow(name=TOPUP_PAGE)]
for screen in screens:
    program.add_widget(screen)

program.current = FIRST_PAGE

class MainApp(App):
    def build(self):
        return program