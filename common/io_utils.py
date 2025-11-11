def read_lines(path: str) -> list[str]:
    #Зчитує файл построково та повертає список рядків без символів \n.
    #Якщо файл не існує — виводить повідомлення і повертає порожній список.

    lines = []

    try:
        # Відкриваємо файл у режимі читання
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                lines.append(line.strip())
    except FileNotFoundError:
        # Якщо файл не існує:
        print("Файл не знайдено.")
        return []
    except Exception as e:
        # Будь-яка інша непередбачена помилка
        print(f"Помилка: {e}")
        return []

    return lines
