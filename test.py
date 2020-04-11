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
from variable import kv, program, db
from util import invalidForm, invalidLogin, invalidPurchase

kv = Builder.load_file("my.kv")

if __name__ == "__main__":
    MyMainApp().run()