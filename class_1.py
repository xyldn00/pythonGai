class Soda:
    def __init__(self, additive=None):
        self.additive = additive

    def show_my_drink(self):
        if self.additive:
            print(f"Газировка и {self.additive}")
        else:
            print("Обычная газировка")

#Пример 

drink1 = Soda("лимон")
drink1.show_my_drink()   


# init - Метод-конструктор. Вызывается автоматически при создании объекта. Настраивает начальные значения
# self - Ссылка на сам объект. Позволяет обращаться к его атрибутам и методам
# Атрибут - Переменная, принадлежащая объекту (например, self.balance)
# Метод - Функция, принадлежащая классу (например, show_my_drink()) 

#Еще есть pass в ООП на python , он нужен для того, чтобы запустить класс без кода, 
#пример 
#class GAI:
#     pass 


