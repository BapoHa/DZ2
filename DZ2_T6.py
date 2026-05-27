def get_cats_info(path):
    cats = []
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                cat_id, name, age = line.split(",")
                cats.append({"id": cat_id, "name": name, "age": age})

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
    except ValueError:
        print("Файл пошкоджений або має неправильний формат.")

    return cats


path = input("Введіть шлях до файлу: ").strip()
cats_info = get_cats_info(path)
print(cats_info)
