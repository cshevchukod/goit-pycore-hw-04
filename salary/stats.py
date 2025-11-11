def sum_and_avg(values: list[int]) -> tuple[int, int]:
    
    #Обчислює загальну суму та середню зарплату.
    #Якщо список порожній — повертає (0, 0).
    
    if not values:         # якщо список порожній
        return 0, 0

    # Підрахунок загальної суми
    total = sum(values)

    # Цілочисельне середнє (без дробової частини)
    avg = total // len(values)

    # Повертаємо кортеж (загальна, середня)
    return total, avg
