from group_limit_reached_exception import GroupLimitReachedException


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
