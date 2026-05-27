def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Контакт додано."


def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return "Контакт не знайдено."
    contacts[name] = phone
    return "Контакт оновлено."


def show_phone(args, contacts):
    name = args[0]
    if name not in contacts:
        return "Контакт не знайдено."
    return contacts[name]


def show_all(contacts):
    if not contacts:
        return "Контакти не знайдено."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def show_help():
    commands = [
        "hello / hi                     - привітання",
        "add <ім'я> <телефон>           - додати контакт",
        "change <ім'я> <телефон>        - змінити номер контакту",
        "phone <ім'я>                   - показати номер контакту",
        "all                            - показати всі контакти",
        "help                           - список команд",
        "close / exit / bye             - завершити роботу",
    ]
    return "Доступні команди:\n" + "\n".join(commands)


def main():
    contacts = {}
    print("Ласкаво просимо до бота-помічника! Введіть команду 'help' для перегляду доступних команд.")
    while True:
        user_input = input("Введіть команду: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "bye"]:
            print("Допобачення!")
            break
        elif command in ["hello", "hi"]:
            print("Привіт! Як я можу допомогти?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "help":
            print(show_help())
        else:
            print("Невідома команда.")


if __name__ == "__main__":
    main()
