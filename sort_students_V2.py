class Students:
    def __init__(self, full_name, group_number, progress):
        self.full_name = full_name
        self.group_number = group_number
        self.progress = progress

# Обычная функция для получения ключа сортировки (по имени)
def sort_by_name(student):
    return student.full_name

# Ввод количества студентов
n = int(input("Кол-во студентов: "))
students = []

# Сбор данных о студентах
for i in range(n):
    print(f"\n--- Студент {i + 1} ---")
    full_name = input("Имя студента: ")
    group_number = input("Группа студента: ")
    
    progress = []
    for j in range(3):
        progress.append(int(input(f"Введите оценку {j + 1}: ")))
        
    # Добавляем нового студента в список
    students.append(Students(full_name, group_number, progress))

students = sorted(students, key=sort_by_name)

# Вывод результатов
print("\nСтуденты с неудовлетворительными оценками:")
found = False

for st in students:
    # Проверяем наличие двоек (если нужны любые оценки ниже 3, используйте: any(grade < 3 for grade in st.progress))
    if 2 in st.progress:
        print(f"Группа: {st.group_number} | Студент: {st.full_name}, Оценки: {st.progress}")
        found = True

if not found:
    print("Студентов с неудовлетворительными оценками не найдено.")