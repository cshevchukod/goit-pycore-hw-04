def parse_cats(lines: list[str]) -> list[dict]:
    #Приймає список рядків із файлу, кожен рядок має формат: id,name,age
    #Повертає список словників з ключами:id, name, age

    # Створюємо порожній список, куди будемо додавати дані про кожного кота
    cats = []

    # Перебираємо усі рядки з файлу
    for raw in lines:
        # Пропускаємо порожні рядки
        if not raw:
            continue

        # Розділяємо рядок на три частини: id, name, age
        temp_list = raw.split(',', 2)  # розбиваємо рядок на максимум 3 частини
        parts = []
        for p in temp_list:
            parts.append(p.strip())    # видаляємо пробіли та додаємо у список

        # Якщо у рядку менше трьох частин — пропускаємо його
        if len(parts) != 3:
            continue

        # Розпаковуємо елементи списку parts у три змінні
        cid, name, age = parts

        # Перевіряємо, що всі частини непорожні
        if not cid or not name or not age:
            continue

        # Перевіряємо, що вік — це число
        if not age.isdigit():
            continue

        # Додаємо словник у список котів
        cats.append({"id": cid, "name": name, "age": age})

    # Повертаємо готовий список усіх валідних записів
    return cats
