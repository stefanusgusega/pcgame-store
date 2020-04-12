from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from backend import Database

from WindowManager import WindowManager

program = WindowManager()
db = Database("users.txt")

class DownloadWindow(Screen):
    def download(self):
        pop = Popup(title='Download game',
                  content=Label(text='ini linknya'),
                  size_hint=(None, None), size=(500, 200))
        pop.open()