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
from MainApp import MainApp

from constant import LOGIN_PAGE, REGISTER_PAGE, MAIN_PAGE, PURCHASE_PAGE, DOWNLOAD_PAGE,GAME_PAGE, FIRST_PAGE, PROFILE_PAGE, HELP_PAGE, TOPUP_PAGE
from backend import Database
from util import invalidForm, invalidLogin, invalidPurchase

if __name__ == "__main__":
    MainApp().run()