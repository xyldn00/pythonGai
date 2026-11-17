class User:
    def __init__(self, login: str, password: str, secret_phrase: str):
        self.login = login
        self.password = password  # Сразу вызывает сеттер для проверки
        self.__secret_phrase = secret_phrase  # Приватная фраза

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой")
        if not (5 <= len(value) <= 12):
            raise ValueError("Длина пароля должна быть от 5 до 12 символов")
        if not any(char.isdigit() for char in value):
            raise ValueError("В пароле должна быть хотя бы одна цифра")

        self._password = value

    def get_secret_phrase(self, password: str) -> str:
        if password == self._password:
            return self.__secret_phrase
        return "Неверный пароль!"


# --- 1. Создание пользователя вручную через консоль ---
while True:
    try:
        login_input = input("Придумай логин: ")
        password_input = input("Придумай пароль (5-12 символов, мин. 1 цифра): ")
        phrase_input = input("Введи секретную фразу: ")

        # Пытаемся создать объект с введёнными данными
        user = User(login_input, password_input, phrase_input)
        print(f"\nПользователь '{user.login}' успешно создан!\n")
        break
    except (TypeError, ValueError) as e:
        print(f"Ошибка при создании: {e}. Попробуй ещё раз.\n")


# --- 2. Проверка работы (получение фразы и смена пароля) ---
while True:
    print("Выбери действие:")
    print("1 — Получить секретную фразу")
    print("2 — Сменить пароль")
    print("3 — Выйти")
    choice = input("Твой выбор: ")

    if choice == "1":
        check_pwd = input("Введи пароль: ")
        print("Результат:", user.get_secret_phrase(check_pwd), "\n")

    elif choice == "2":
        new_pwd = input("Введи новый пароль: ")
        try:
            user.password = new_pwd
            print("Пароль успешно изменён!\n")
        except (TypeError, ValueError) as e:
            print(f"Ошибка смены пароля: {e}\n")

    elif choice == "3":
        print("Выход из программы.")
        break

    else:
        print("Неизвестная команда, выбери 1, 2 или 3.\n")
