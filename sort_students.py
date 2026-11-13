class Students:

  def __init__(self, full_name, group_number, progress):
    self.full_name = full_name
    self.group_number = group_number
    self.progress = progress


# Обычная функция для получения ключа сортировки
def sort_by_name(student):
  return student.full_name


# Исходный список студентов
students = [
    Students("Павел", "Повар", [2, 3, 5]),
    Students("Петр", "Повар", [4, 3, 5]),
    Students("Вася", "3467/1", [2, 4, 3]),
    Students("Коля Камызяка", "3467/1", [2, 2, 2]),
]

# Сначала сортируем список по имени
students = sorted(students, key=sort_by_name)

print("Студенты с неудовлетворительными оценками:")

# Затем проходим по отсортированному списку и выводим тех, у кого есть двойки (< 3)
for st in students:
  if any(grade < 3 for grade in st.progress):
    print(st.full_name, st.progress)