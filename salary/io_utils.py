from pathlib import Path   # для перевірки існування файлу та роботи з шляхами

def read_lines(path: str) -> list[str]:
    #Зчитує файл построково та повертає список рядків без символів \n.
    #Якщо файл не існує — виводить повідомлення і повертає порожній список.
    
    path_obj = Path(path)           # створюємо об'єкт шляху

    # Перевіряємо, чи існує файл
    if not path_obj.exists():
        print("Файл не знайдено.")
        return []

    lines = []

    # Відкриваємо файл у режимі читання
    with open(path_obj, 'r', encoding='utf-8') as file:
        # Зчитуємо рядки по одному і видаляємо символи переводу рядка
        for line in file:
            lines.append(line.strip())

    # Повертаємо список усіх рядків
    return lines
