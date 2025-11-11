def parse_salaries(lines: list[str]) -> list[int]:
    #Приймає список рядків типу 'Name,3000'.
    #Ігнорує порожні або некоректні рядки.
    #Повертає список чисел (зарплат).
    
    salaries = []

    # Перебираємо кожен рядок із файлу
    for line in lines:
        if not line:              # якщо рядок порожній — пропускаємо
            continue
        if ',' not in line:       # якщо немає коми — це не зарплата
            continue

        # Розділяємо рядок: ім'я та значення
        name, value = line.split(',', 1)
        value = value.strip()     # прибираємо зайві пробіли

        # Перевіряємо, чи друга частина — число
        if value.isdigit():
            salaries.append(int(value))   # додаємо в список як число

    # Повертаємо всі валідні зарплати
    return salaries
