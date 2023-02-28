class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def calc_average_rate(self):
        rates = []
        for c in self.courses_in_progress:
            if c in self.grades:
                rates += self.grades[c]
        return sum(rates) / len(rates)

    def __str__(self):
        average_rate = self.calc_average_rate()
        cip = ", ".join(self.courses_in_progress)
        fc = ", ".join(self.finished_courses)
        return f'Имя:{self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {average_rate}\n' \
               f'Курсы в процессе изучения: {cip} \n' \
               f'Завершенные курсы: {fc}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def calc_average_rate(self):
        rates = []
        for course_grade in self.grades:
            rates += self.grades[course_grade]

        return sum(rates) / len(rates)

    def __str__(self):
        return f'Имя:{self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.calc_average_rate()}'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.calc_average_rate(self) > Lecturer(other).calc_average_rate(other)
        return 'Ошибка'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя:{self.name}\nФамилия: {self.surname}'


def calc_students_average_rate(students, course):
    rates = []
    for student in students:
        if isinstance(student, Student):
            if course in student.grades:
                rates += student.grades[course]
    return sum(rates) / len(rates)


def calc_lectors_average_rate(lectors, course):
    rates = []
    for lector in lectors:
        if isinstance(lector, Lecturer):
            if course in lector.grades:
                rates += lector.grades[course]
    return sum(rates) / len(rates)



Student1 = Student("Василий", "Теркин", "М")
Student2 = Student("Василиса", "Премудрая", "Ж")

Lecturer1 = Lecturer("Иван", "Иванов")
Lecturer2 = Lecturer("Петр", "Петров")

Reviewer1 = Reviewer("Дарт", "Вэйдер")
Reviewer2 = Reviewer("Йода", "Мастер")

_python_ = 'Python'
_c_ = 'C#'
_java_ = 'Java'

Student1.courses_in_progress.append(_python_)
Student1.courses_in_progress.append(_c_)
Student1.courses_in_progress.append(_java_)
Student1.finished_courses.append("курсы кройки и шитья")
Student1.finished_courses.append("Введение в программирование")

Student2.courses_in_progress.append(_python_)
Student2.courses_in_progress.append(_c_)
Student2.courses_in_progress.append(_java_)
Student2.finished_courses.append("Компьютерная грамотность")
Student2.finished_courses.append("Введение в программирование")

Lecturer1.courses_attached.append(_python_)
Lecturer1.courses_attached.append(_java_)
Lecturer2.courses_attached.append(_c_)
Lecturer2.courses_attached.append(_java_)

Reviewer1.courses_attached.append(_python_)
Reviewer1.courses_attached.append(_c_)
Reviewer2.courses_attached.append(_python_)
Reviewer2.courses_attached.append(_java_)

students = [Student1, Student2]
lectors = [Lecturer1, Lecturer2]

Student1.rate_lecturer(Lecturer1, _python_, 4)
Student1.rate_lecturer(Lecturer1, _java_, 5)
Student1.rate_lecturer(Lecturer2, _c_, 5)
Student1.rate_lecturer(Lecturer2, _java_, 5)

Student2.rate_lecturer(Lecturer1, _python_, 3)
Student2.rate_lecturer(Lecturer1, _java_, 3)
Student2.rate_lecturer(Lecturer2, _c_, 4)
Student2.rate_lecturer(Lecturer2, _java_, 3)

Reviewer1.rate_hw(Student1, _python_, 4)
Reviewer1.rate_hw(Student1, _c_, 2)
Reviewer1.rate_hw(Student2, _python_, 4)
Reviewer1.rate_hw(Student2, _c_, 4)

Reviewer2.rate_hw(Student1, _python_, 5)
Reviewer2.rate_hw(Student1, _java_, 5)
Reviewer2.rate_hw(Student2, _python_, 4)
Reviewer2.rate_hw(Student2, _java_, 4)

print("Student1")
print(Student1)
print("\r")
print("Student2")
print(Student2)
print("\r")
print("Reviewer1")
print(Reviewer1)
print("\r")
print("Reviewer2")
print(Reviewer2)
print("\r")
print("Lecturer1")
print(Lecturer1)
print("\r")
print("Lecturer2")
print(Lecturer2)
print("\r")

sarPython = calc_students_average_rate(students, _python_)
sarC = calc_students_average_rate(students, _c_)
sarJava = calc_students_average_rate(students, _java_)
print("Students average rate for Python:", sarPython)
print("Students average rate for C#:", sarC)
print("Students average rate for Java:", sarJava)
print("\r")

larPython = calc_lectors_average_rate(lectors, _python_)
larC = calc_lectors_average_rate(lectors, _c_)
larJava = calc_lectors_average_rate(lectors, _java_)
print("Lectors average rate for Python:", larPython)
print("Lectors average rate for C#:", larC)
print("Lectors average rate for Java:", larJava)
