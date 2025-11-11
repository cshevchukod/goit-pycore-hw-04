from salary import total_salary   # імпортуємо головну функцію з пакета salary

def main() -> None:
    #Точка входу.
    #Викликає total_salary() і виводить результат.
    
    total, average = total_salary("path/to/salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


# Перевіряємо, що скрипт запущено напряму, а не імпортовано
if __name__ == "__main__":
    main()
