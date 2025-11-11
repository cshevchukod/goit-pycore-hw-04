from salary import total_salary   # імпортуємо головну функцію з пакета salary
from cats import get_cats_info    # імпортуємо головну функцію з пакета cats

def main() -> None:
    #Точка входу.
    #Викликає total_salary() і виводить результат.
    
    total, average = total_salary("path/to/salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

    #Викликає get_cats_info() і виводить результат.
    cats_info = get_cats_info("path/to/cats_file.txt")
    print(cats_info)


# Перевіряємо, що скрипт запущено напряму, а не імпортовано
if __name__ == "__main__":
    main()
