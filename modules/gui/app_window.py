"""
    Цей файл використовується для створення вікна додатку
"""

# імпортуємо модулі
import customtkinter as ctk
from ..tools import read_json, create_media_folder

# Створюємо клас, який наслідуємо від ctk.CTk
class App(ctk.CTk):
    """
        Цей клас відповідає за вікно додатку
    """
    
    def __init__(self, **kwargs):
        """
            Ця функція - це конструктор класу
        """
        
        create_media_folder()
        json_data = read_json(name_json="settings.json")
        
        
        # наслідуємо конструктор класу-батька
        ctk.CTk.__init__(self,fg_color = json_data["app_fg_color"],**kwargs)
        
        # Створюємо свойства ширини та висоти. Ширина і висота = 80% від ширини та висоти монітору користувача
        # winfo_screenwidth() - функція, яка отримує ширину монітора користувача
        # winfo_screenheight() - функція, яка отримує висоту монітора користувача
        # Перетворюэмо розміри в int, бо функція geometry працює тільки з int
        self.width = int(self.winfo_screenwidth() * json_data["app_width"])
        self.height = int(self.winfo_screenheight() * json_data["app_height"])
        # функція title встановлює назву вікна
        self.title(json_data["app_title"])
        # функція geometry задає розміри вікна
        self.geometry(f"{self.width}x{self.height}")
        
        
# створюємо екземпляр (об'єкт) класу App.
# Тобто створюємо вікно додатку  
app = App()






