def parse_cats(lines: list[str]) -> list[dict]:
    #Приймає рядки формату id,name,age.
    #Ігнорує порожні/биті рядки.
    #Повертає список словників з ключами: id, name, age.
    cats = []

    for raw in lines:
        if not raw:
            continue

        # максимум 2 розділення, щоб не роз'їхалось, якщо в name буде кома
        parts = [p.strip() for p in raw.split(',', 2)]
        if len(parts) != 3:
            continue

        cid, name, age = parts

        # базова валідація
        if not cid or not name or not age:
            continue
        # в прикладі вік — рядок; якщо треба число, легко перетворити на int
        if not age.isdigit():
            continue

        cats.append({"id": cid, "name": name, "age": age})

    return cats
