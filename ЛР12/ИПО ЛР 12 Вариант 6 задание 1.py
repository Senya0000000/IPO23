class Student:
    def __init__(self, name, group_number, otmetki):
        self.name = name
        self.group_number = group_number
        self.otmetki = otmetki
    def has_failing_otmetki(self):
        for otmetki in self.otmetki:
            if otmetki < 4:  # Предположим, что неудовлетворительная отметка начинается с 4
                return True
        return False
# Создаем массив из десяти структур типа Student
students = []
for _ in range(10):
    name = input("Введите фамилию и инициалы студента: ")
    group_number = input("Введите номер группы: ")
    otmetki = [int(input(f"Введите оценку {i + 1}: ")) for i in range(5)]
    students.append(Student(name, group_number, otmetki))
# Выводим фамилии и номера групп студентов с хотя бы одной неудовлетворительной отметкой
found_failing = False
for student in students:
    if student.has_failing_otmetki():
        print(f"Студент {student.name} из группы {student.group_number} имеет неудовлетворительные отметки.")
        found_failing = True
if not found_failing:
    print("У всех студентов хорошая успеваемость!")