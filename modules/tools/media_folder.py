"""
    Цей модуль створює папку media
"""
# імпортуємо модулі
import colorama
import os
# робимо так, щоб після кожного рядку колір скидувався
colorama.init(autoreset=True)

# Задаємо константи для кольорів
GREEN = colorama.Fore.GREEN
RED = colorama.Fore.RED
YELLOW = colorama.Fore.YELLOW

def create_media_folder():
    """
        Ця функція створює папку media
    """
    # намагаємось щось зробити, якщо буде помилка - ідемо в exception
    try:
        # знаходимо абсолютний шлях до папки медіа
        # join - об'єднує шляхи
        # abspath - нормалізує шляхи (прибирає зайві ../../)
        # __file__ - "магічна" змінна, яка зберігає абсолютний шлях до файлу
        path_media = os.path.abspath(os.path.join(__file__, "..", "..", "..", "media"))
        # перебираємо список, у якому зберігаються назви двох папок, які будуть створені у папці media
        for dir in ["downloaded_images", "edited_images"]:
            # Якщо папки dir у папці media не існує, то заходимо в тіло умови
            if os.path.exists(os.path.join(path_media, dir)) == False:
                # Робимо папку dir у папці media.
                # exist_ok = True означає, що якщо всі папки вже створені, то помилки не буде.
                os.makedirs(os.path.join(path_media, dir), exist_ok=True)
                print(f"{GREEN}{dir} в папці media було створено")
    # якщо виникає помилка, то виводимо у консоль помилку
    except Exception as exception:
        print(f"{RED}Сталася помилка при створенні директорії media: {exception}")
        
