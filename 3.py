class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def add(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Пополнение на {amount}. Баланс: {self.balance}")
        else:
            print("Сумма пополнения должна быть положительной!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств на счете!")
        elif amount <= 0:
            print("Сумма снятия должна быть положительной!")
        else:
            self.balance -= amount
            print(f"Снятие {amount}. Баланс: {self.balance}")

#Пример 
account = BankAccount("123456789", 1000)

account.add(500)
account.withdraw(200)    
account.withdraw(2000)   