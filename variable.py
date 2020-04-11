from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from backend import Database

from constant import *

import FirstWindow
import RegisterUserWindow
import LoginUserWindow
import MainWindow
import PurchaseWindow
import DownloadWindow
import GameDetailsWindow
import WindowManager
import MyMainApp

kv = Builder.load_file("my.kv")
db = Database("users.txt")
program = WindowManager()
screens = [LoginUserWindow(name=LOGIN_PAGE), RegisterUserWindow(name=REGISTER_PAGE), MainWindow(name=MAIN_PAGE),PurchaseWindow(name=PURCHASE_PAGE),DownloadWindow(name=DOWNLOAD_PAGE),GameDetailsWindow(name=GAME_PAGE),FirstWindow(name=FIRST_PAGE)]

for screen in screens:
    program.add_widget(screen)

program.current = FIRST_PAGE