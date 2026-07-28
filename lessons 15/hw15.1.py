class GroupLimitReachedException(Exception):
    def __init__(self, error_message, group_name):
        self.error_message = error_message
        self.group_name = group_name

    def __str__(self):
        return f"{self.error_message} (group: {self.group_name})"


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.gender} {self.age}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return super().__str__() + f' {self.record_book}'


class Group:
    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.MAX_STUDENTS:
            raise GroupLimitReachedException(
                f"Cannot add student, group limit ({self.MAX_STUDENTS}) reached", self.number
            )
        self.group.add(student)

    def delete_student(self, last_name):
        for student in self.group.copy():
            if student.last_name == last_name:
                self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += f"\n{student}"
        return f'Number:{self.number}\n{all_students}'


# Перевірка
group = Group('PD1')

try:
    for i in range(11):    # намагаємось додати 11 студентів
        student = Student('Male', 20, f'Name{i}', f'Surname{i}', f'AN{i}')
        group.add_student(student)
    print("Всі 11 студентів додано без помилки")   # сюди дійти не повинно
except GroupLimitReachedException as error:
    print(f"Помилка: {error}")

print(f"Студентів у групі: {len(group.group)}")