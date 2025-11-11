# Імпортуємо допоміжні функції з інших модулів пакета
from .io_utils import read_lines
from .parse import parse_salaries
from .stats import sum_and_avg

def total_salary(path: str) -> tuple[int, int]:
    #Основна функція пакета:
    #1. Зчитує файл
    #2. Розбирає рядки на зарплати
    #3. Обчислює суму та середнє значення
    #Повертає кортеж (загальна, середня)
    
    # Зчитуємо всі рядки з файлу
    lines = read_lines(path)

    # Якщо файл не знайдено або порожній — повертаємо 0, 0
    if not lines:
        return 0, 0

    # Парсимо зарплати у числа
    salaries = parse_salaries(lines)

    # Рахуємо загальну суму та середнє
    total, avg = sum_and_avg(salaries)

    # Повертаємо результат у вигляді кортежу
    return total, avg
