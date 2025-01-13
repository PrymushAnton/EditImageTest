"""
    Цей модуль використовується для того, щоб створити вікно додатку
"""

import customtkinter as ctk
from ..tools import read_json


class App(ctk.CTk):
    """
        Цей клас - базова структура вікна додатку
    """
    
    def __init__(self):
        """
            Це конструктор класу, за допомогою якого задаються 
            налаштування основного вікна програми
        """
        
        self.SETTINGS = read_json("config.json")
        
        ctk.CTk.__init__(self, fg_color=self.SETTINGS["app_fg_color"])
        
        
        self.WIDTH = int(self.winfo_screenwidth() * self.SETTINGS["app_width"])
        self.HEIGHT = int(self.winfo_screenheight() * self.SETTINGS["app_height"])
        
        self.title(self.SETTINGS["app_title"])
        
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        
app = App()



