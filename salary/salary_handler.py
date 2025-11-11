import pathlib
from .utils import parse_line


def total_salary(path):
    try:
        path_obj = pathlib.Path(path)
        if not path_obj.exists():
            print("Файл не знайдено.")
            return (0, 0)

        with open(path_obj, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                salary = parse_line(line)
                if salary is not None:
                    salaries.append(salary)

        if not salaries:
            return (0, 0)

        total = sum(salaries)
        average = total // len(salaries)
        return total, average

    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return (0, 0)
