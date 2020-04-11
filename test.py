from kivy.lang import Builder

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
from MyMainApp import MyMainApp

from constant import LOGIN_PAGE, REGISTER_PAGE, MAIN_PAGE, PURCHASE_PAGE, DOWNLOAD_PAGE,GAME_PAGE, FIRST_PAGE,PROFILE_PAGE,HELP_PAGE,TOPUP_PAGE
from backend import Database
from util import invalidForm, invalidLogin, invalidPurchase

kv = Builder.load_file("my.kv")
program = WindowManager()
db = Database("users.txt")

screens = [LoginUserWindow(name=LOGIN_PAGE), RegisterUserWindow(name=REGISTER_PAGE), MainWindow(name=MAIN_PAGE),PurchaseWindow(name=PURCHASE_PAGE),DownloadWindow(name=DOWNLOAD_PAGE),GameDetailsWindow(name=GAME_PAGE),FirstWindow(name=FIRST_PAGE),ProfileWindow(name=PROFILE_PAGE),HelpWindow(name=HELP_PAGE),TopUpWindow(name=TOPUP_PAGE)]
for screen in screens:
    program.add_widget(screen)

if __name__ == "__main__":
    MyMainApp().run()