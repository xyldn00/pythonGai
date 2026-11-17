phonebook = {}

while True:
    print("\n--- Телефонная книга ---")
    print("1. Добавить контакт")
    print("2. Найти контакт")
    print("3. Удалить контакт")
    print("4. Показать все контакты")
    print("5. Выход")

    choice = input("Выберите действие (1-5): ")

    if choice == "1":   
        name = input("Введите имя: ")
        phone = input("Введите номер телефона: ")
        phonebook[name] = phone
        print(f"Контакт '{name}' сохранен.")

    elif choice == "2":
        name = input("Введите имя для поиска: ")
        if name in phonebook:
            print(f"Номер {name}: {phonebook[name]}")
        else:
            print("Контакт не найден.")

    elif choice == "3":
        name = input("Введите имя для удаления: ")
        if name in phonebook:
            del phonebook[name]
            print(f"Контакт '{name}' удален.")
        else:
            print("Контакт не найден.")

    elif choice == "4":
        if phonebook:
            print("\nСписок всех контактов:")
            for name, phone in phonebook.items():
                print(f"- {name}: {phone}")
        else:
            print("Телефонная нига пуста.")

    elif choice == "5":
        print("Выход из программы.")
        break 
    
    else:
        print("Неверный ввод, выберите пункт от 1 до 5.")