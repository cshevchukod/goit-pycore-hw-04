# Скрипт для відображення структури директорії (дерева тек і файлів)
# Виклик у терміналі:
#     python hw03.py /шлях/до/директорії

import sys
from pathlib import Path
from colorama import init, Fore, Style

# Кольори для виводу
DIR = Fore.CYAN + Style.BRIGHT   # колір для тек
FILE = Fore.YELLOW               # колір для файлів


def _print_tree(root: Path, indent: str = "") -> None:
    #Рекурсивно проходить по всіх елементах директорії.
    #Виводить теки і файли з відступами.

    # Допоміжна функція, що визначає, як сортувати елементи
    def sort_key(p: Path):
        # Повертаємо кортеж (is_file, name), щоб спочатку йшли теки, потім файли
        return (p.is_file(), p.name.lower())

    # Створюємо список елементів у поточній теці
    entries = []

    try:
        for element in root.iterdir():
            entries.append(element)

        # Сортуємо елементи за допомогою нашої функції sort_key
        entries.sort(key=sort_key)

        # Перебираємо всі елементи і виводимо їх
        for p in entries:
            if p.is_dir():
                # Якщо це тека — виводимо її і викликаємо функцію знову (рекурсія)
                print(indent + DIR + f"{p.name}/" + Style.RESET_ALL)
                _print_tree(p, indent + "    ")
            else:
                # Якщо це файл — просто виводимо ім’я
                print(indent + FILE + p.name + Style.RESET_ALL)

    except Exception as e:
        # Якщо виникла будь-яка помилка — виводимо її текст
        print(f"Помилка: {e}")
        return

def hw03_main() -> None:
    #Основна функція:
    #1. Отримує шлях до директорії з аргументів командного рядка.
    #2. Перевіряє, що шлях існує і це тека.
    #3. Викликає функцію для виводу структури.

    # Якщо користувач не передав шлях
    if len(sys.argv) < 2:
        print("Використання: python hw03.py шлях_до_директорії")
        return

    # Отримуємо шлях із аргументів
    user_input = sys.argv[1]

    # Створюємо об’єкт Path для зручної роботи
    target = Path(user_input)

    # Перевіряємо, чи існує шлях
    if not target.exists():
        print("Помилка: шлях не існує.")
        return

    # Перевіряємо, чи це директорія
    if not target.is_dir():
        print("Помилка: вказано не директорію.")
        return

    # Ініціалізуємо colorama (щоб кольори працювали однаково на всіх ОС)
    init(autoreset=True)

    # Виводимо назву кореневої теки
    print(DIR + f"{target.resolve().name}/" + Style.RESET_ALL)

    # Запускаємо рекурсивний обхід і вивід
    _print_tree(target)


# Виконуємо main(), якщо скрипт запущено напряму
if __name__ == "__main__":
    # Якщо файл запущено напряму, запускаємо основний цикл
    hw03_main()

