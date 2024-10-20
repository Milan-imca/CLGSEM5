'''1
• Create classes Employee, Manager, and Developer.
• Classes Manager and Developer inherits Employee.
• Create appropriate methods to get details and display details for all classes.
• Implement constructors and destructors for same.
• Modify the Employee class to include a method that calculates a bonus based on the salary.
• Modify the Manager and Developer classes to utilize this method.
• Add a new class called Intern that also inherits from Employee.
• The Intern class should have an additional attribute duration (in months).
• Implement methods to display intern details and calculate a stipend based on the duration.
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"Employee {self.name} created.")

    def __del__(self):
        print(f"Employee {self.name} deleted.")

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"

    def display_details(self):
        print(self.get_details())

    def calculate_bonus(self):
        return self.salary * 0.10  # 10% bonus


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
        print(f"Manager {self.name} created with team size {self.team_size}.")

    def __del__(self):
        print(f"Manager {self.name} deleted.")

    def get_details(self):
        return f"{super().get_details()}, Team Size: {self.team_size}"

    def display_details(self):
        print(self.get_details())
        bonus = self.calculate_bonus()
        print(f"Bonus: {bonus}")


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
        print(f"Developer {self.name} created, programming in {self.programming_language}.")

    def __del__(self):
        print(f"Developer {self.name} deleted.")

    def get_details(self):
        return f"{super().get_details()}, Programming Language: {self.programming_language}"

    def display_details(self):
        print(self.get_details())
        bonus = self.calculate_bonus()
        print(f"Bonus: {bonus}")


class Intern(Employee):
    def __init__(self, name, salary, duration):
        super().__init__(name, salary)
        self.duration = duration
        print(f"Intern {self.name} created for {self.duration} months.")

    def __del__(self):
        print(f"Intern {self.name} deleted.")

    def get_details(self):
        return f"{super().get_details()}, Duration: {self.duration} months"

    def display_details(self):
        print(self.get_details())
        stipend = self.calculate_stipend()
        print(f"Stipend: {stipend}")

    def calculate_stipend(self):
        return self.salary * 0.05 * self.duration  # 5% of salary per month


emp = Employee("Alice", 50000)
emp.display_details()

mgr = Manager("Bob", 80000, 5)
mgr.display_details()

dev = Developer("Charlie", 60000, "Python")
dev.display_details()

intern = Intern("Dave", 20000, 6)
intern.display_details()
