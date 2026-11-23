import math


class Car:
    def __init__(self, x: float = 0.0, y: float = 0.0, angle: float = 0.0):
        # Начальные координаты и угол направления движения (в градусах)
        self.x = x
        self.y = y
        self.angle = angle

    def turn(self, delta_angle: float):
        # Поворачиваем на delta_angle градусов; % 360 удерживает угол в диапазоне [0, 360)
        self.angle = (self.angle + delta_angle) % 360

    def move(self, distance: float):
        # Переводим угол из градусов в радианы для тригонометрических функций math
        radians = math.radians(self.angle)
        self.x += distance * math.cos(radians)
        self.y += distance * math.sin(radians)


class Bus(Car):
    def __init__(self, x: float = 0.0, y: float = 0.0, angle: float = 0.0, fare_per_km: float = 10.0):
        # Вызываем конструктор родительского класса Car, чтобы инициализировать x, y и angle
        super().__init__(x, y, angle)
        # Поля, специфичные для автобуса: изначально пассажиров 0 и денег 0
        self.passengers = 0
        self.money = 0.0
        self.fare_per_km = fare_per_km

    def enter(self, count: int = 1):
        if count < 0:
            raise ValueError("Количество вошедших пассажиров не может быть отрицательным")
        self.passengers += count

    def exit(self, count: int = 1):
        if count < 0:
            raise ValueError("Количество вышедших пассажиров не может быть отрицательным")
        # max(0, ...) гарантирует, что число пассажиров не уйдёт в минус
        self.passengers = max(0, self.passengers - count)

    # Переопределение метода (overriding) — ещё одна форма полиморфизма:
    # метод называется так же, как у Car, но работает по-своему для Bus
    def move(self, distance: float):
        # Сначала выполняем базовое перемещение из Car (обновляем x и y)
        super().move(distance)
        # Затем добавляем выручку: пассажиры * расстояние * стоимость за км
        self.money += self.passengers * distance * self.fare_per_km


# Полиморфный список транспортных средств: и Car, и Bus имеют общий метод move()
vehicles = [
    Car(0, 0, 0),
    Bus(0, 0, 0, fare_per_km=5.0),
]

vehicles[0].move(10)
vehicles[0].turn(90)
vehicles[0].move(5)

vehicles[1].enter(12)
vehicles[1].move(4)   # 12 * 4 * 5 = 240
vehicles[1].exit(2)
vehicles[1].turn(90)
vehicles[1].move(6)   # 10 * 6 * 5 = 300 -> всего 540

# Единый вызов v.move(1) для разных типов объектов (полиморфизм)
for v in vehicles:
    v.move(1)

print(f"Автомобиль: координаты=({vehicles[0].x:.2f}, {vehicles[0].y:.2f}), угол={vehicles[0].angle}°")
print(
    f"Автобус: координаты=({vehicles[1].x:.2f}, {vehicles[1].y:.2f}), "
    f"пассажиров={vehicles[1].passengers}, деньги={vehicles[1].money:.2f}"
)