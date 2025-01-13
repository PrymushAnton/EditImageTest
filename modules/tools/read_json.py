"""
    Цей файл використовується для того, щоб отримати дані з файлу json
"""

import json
from os.path import abspath, join
import colorama
colorama.init(autoreset=True)

RED = colorama.Fore.RED
YELLOW = colorama.Fore.YELLOW

def read_json(name_json: str) -> dict:
    """
        Ця функція використовується для отримання даних з файлу json
    """
    
    try:
        path_to_json = abspath(join(__file__, "..", '..', '..', 'static', 'jsons', name_json))
        print(path_to_json)
        with open(path_to_json, "r") as file:
            dict_json = json.load(file)
            return dict_json
        
    except Exception as exception:
        print(f"{RED}Не існує файлу {YELLOW}{name_json}")
        return {}




