class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

class Teacher(Employee):
    def __init__(self, name, emp_id, subjects):
        super().__init__(name, emp_id)
        self.subjects = subjects
    def teach(self):
        print(self.name, "is teaching:", ", ".join(self.subjects))

class AdminStaff(Employee):
    def __init__(self, name, emp_id, designation):
        super().__init__(name, emp_id)
        self.designation = designation
    def admin_task(self):
        print(self.name, "is doing administrative work as", self.designation)

class TeacherAdmin(Teacher, AdminStaff):
    def __init__(self, name, emp_id, subjects, designation):
        Teacher.__init__(self, name, emp_id, subjects)
        self.designation = designation

t1 = Teacher("Rahul", 101, ["Python", "Math"])
a1 = AdminStaff("Anita", 102, "Office Manager")
ta1 = TeacherAdmin("Ramesh", 103, ["Java", "C++"], "HOD")

print("Teacher Details")
print("Name:", t1.name)
print("ID:", t1.emp_id)
t1.teach()

print()

print("Admin Staff Details")
print("Name:", a1.name)
print("ID:", a1.emp_id)
a1.admin_task()

print()

print("TeacherAdmin Details")
print("Name:", ta1.name)
print("ID:", ta1.emp_id)
print("Designation:", ta1.designation)
ta1.teach()
ta1.admin_task()

print()

print("Method Resolution Order (MRO)")
print(TeacherAdmin.__mro__)