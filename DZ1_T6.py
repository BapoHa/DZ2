def total_salary(path):
    try:
        with open(path, encoding="utf-8") as f:
            salaries = []
            for line in f:
                line = line.strip()
                if not line:
                    continue
                name, salary = line.split(",")
                salaries.append(int(salary))

        if not salaries:
            return 0, 0

        total = sum(salaries)
        average = total // len(salaries)
        return total, average

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return 0, 0
    except ValueError:
        print("Файл пошкоджений або має неправильний формат.")
        return 0, 0


path = input("Введіть шлях до файлу: ").strip()
total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
