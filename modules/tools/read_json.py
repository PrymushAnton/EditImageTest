"""
    Цей файл використовується для читання json файлу
"""
# Імпортуємо модулі
import json
import os
import colorama
colorama.init(autoreset=True)

RED = colorama.Fore.RED
YELLOW = colorama.Fore.YELLOW


# створюємо функцію
# name_json: str - це підказка для розробників, що параметр name_json приймає значення типу str
# -> dict - це підказка для розробників, що функція повертає словник
def read_json(name_json: str) -> dict:
    """
        Ця функція використовується для отримання даних з json файлу
    """

    try:
        path_to_json = os.path.abspath(os.path.join(__file__, "..", "..", "..", "static", "jsons", name_json))
        with open(path_to_json, "r") as file:
            dict1 = json.load(file)
            return dict1
    except Exception as exception:
        print(f"{RED}Сталася помилка: {YELLOW}{exception}")
        return {}





