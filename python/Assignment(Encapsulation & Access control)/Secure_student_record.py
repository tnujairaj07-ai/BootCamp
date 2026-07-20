class Student:
    total_students = 0

    def __init__(self, roll_no, marks_list, grade):
        self.__roll_no = roll_no
        self.__marks_list = marks_list
        self._grade = grade

        Student.total_students += 1

    @property
    def gpa(self):
        avg = sum(self.__marks_list) / len(self.__marks_list)
        return avg / 10

    @gpa.setter
    def gpa(self, marks_list):
        for mark in marks_list:
            if mark < 0 or mark > 100:
                raise ValueError("Marks must be between 0 and 100")
        self.__marks_list = marks_list

    @classmethod
    def count(cls):
        return cls.total_students


# Testing
s1 = Student(101, [80, 90, 70], "A")
s2 = Student(102, [85, 75, 95], "A+")

print("GPA of s1:", s1.gpa)

s1.gpa = [88, 92, 79]
print("Updated GPA:", s1.gpa)

print("Total Students:", Student.count())