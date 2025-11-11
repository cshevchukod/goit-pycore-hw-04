# Імпортуємо допоміжні функції з інших модулів пакета
from common.io_utils import read_lines
from .parse import parse_cats

def get_cats_info(path: str) -> list[dict]:
    #Основна функція пакета.
    #1. Зчитує файл.
    #2. Обробляє рядки за допомогою parse_cats().
    #3. Повертає список словників з інформацією про кожного кота.

    # Зчитуємо всі рядки з файлу
    lines = read_lines(path)

    # Якщо файл не знайдено або він порожній — повертаємо порожній список
    if not lines:
        return []
    # Викликаємо функцію, що перетворює рядки у список словників
    return parse_cats(lines)
