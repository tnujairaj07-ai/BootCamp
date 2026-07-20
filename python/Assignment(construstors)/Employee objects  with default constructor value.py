class Employee:
    def __init__(self, name, department="General", bonus=0):
        self.name = name
        self.department = department
        self.bonus = bonus
        self.salary = 30000

    def annual_summary(self):
        total_pay = self.salary + self.bonus
        print("Name:", self.name)
        print("Department:", self.department)
        print("Total Pay:", total_pay)
        print()

emp1 = Employee("Rahul", "IT", 5000)
emp2 = Employee("Priya", "HR")
emp3 = Employee("Amit")

emp1.annual_summary()
emp2.annual_summary()
emp3.annual_summary()