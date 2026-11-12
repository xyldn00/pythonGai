class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    # Геттер
    @property
    def email(self):
        return self.__email

    # Сеттер
    @email.setter
    def email(self, new_email):
        if self.check_email(new_email):
            self.__email = new_email
        else:
            print("Некорректный адрес электронной почты!")

    # Проверка почты
    def check_email(self, email):
        return "@" in email and "." in email.split("@")[-1]


# Создание объекта
user = UserMail("Ivan", "ivan@mail.ru")

print("Логин:", user.login)
print("Почта:", user.email)

# Изменение почты
user.email = "newmail@gmail.com"

print("Новая почта:", user.email)


#__init__ — конструктор, принимает логин и почту.

#@property — геттер, позволяет получить адрес почты.

#@email.setter — сеттер, позволяет изменить почту.

#check_email() — проверяет, есть ли символ @ и точка после него.
