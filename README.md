class User: def init(self, secret_phrase: str): self._password = "" self.__secret_phrase = secret_phrase
#Сделали приватной

@property
def password(self) -> str:
    return self._password

@password.setter
def password(self, value: str) -> None:
    if not isinstance(value, str):
        raise TypeError("Пароль должен быть строкой")
    if not 5 <= len(value) <= 12:
        raise ValueError("Пароль должен быть от 5 до 12 символов")
    if not any(char.isdigit() for char in value):
        raise ValueError("Пароль должен содержать хотя бы одну цифру")
    
    self._password = value

def get_secret_phrase(self, password: str) -> str:
    """Метод возвращает секретную фразу, если пароль введен верно"""
    if password == self._password:
        return self.__secret_phrase
    return "Неверный пароль!"

Создаем объект пользователя

user = User("Тут была секретная фраза!")
1. Ввод и установка пароля (с защитой от дурака)

while True: try: pwd = input("Придумай пароль (5-12 символов, минимум 1 цифра): ") user.password = pwd print("Пароль установлен!\n") break except (TypeError, ValueError) as e: print(f"Ошибка: {e}. Попробуй ещё раз.\n")
2. Проверка пароля

while True: attempt = input("Введи пароль для проверки (или 'exit' для выхода): ")

if attempt.lower() == "exit":
    print("Выход.")
    break

# Пытаемся получить секретную фразу
result = user.get_secret_phrase(attempt)
if result != "Неверный пароль!":
    print(f"Успех! Секретная фраза: {result}")
    break
else:
    print(f"{result}\n")
