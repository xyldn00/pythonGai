class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

# Проверка все ли аргументы числа
    def is_triangle(self):
        if not all(isinstance(i, (int, float)) for i in (self.a, self.b, self.c)):
            return "Нужно вводить только числа!"

        # Проверка отрицательные
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "С отрицательными числами ничего не выйдет!"

        if (self.a + self.b > self.c and
            self.a + self.c > self.b and
            self.b + self.c > self.a):
            return "Ура, можно построить треугольник!"

        return "Жаль, но из этого треугольник не сделать."


# Примерыd
t1 = TriangleChecker(3, 4, 5)
print(t1.is_triangle())  

t2 = TriangleChecker(1, 2, 10)
print(t2.is_triangle()) 
