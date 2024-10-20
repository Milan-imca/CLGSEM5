'''2
• Create classes Person, Student, and Result.
• Classes: Person (base class), Student (inherits from Person), and Result (inherits from
Student).
• Create appropriate methods to get and display details for all classes.
• Implement constructors and destructors for each class.
• Modify the Result class to include a method that calculates and displays the highest and
lowest marks obtained by the student.
• Add a new class called HonorsResult that also inherits from Result.
• The HonorsResult class should have an additional attribute for honors classification (e.g.,
"First Class", "Second Class", etc.).
• Implement methods to display the honors classification and determine if the
• student qualifies for honors based on their average marks.
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person {self.name} created.")

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def __del__(self):
        print(f"Person {self.name} destroyed.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        print(f"Student {self.name} with ID {self.student_id} created.")

    def display_details(self):
        super().display_details()
        print(f"Student ID: {self.student_id}")

    def __del__(self):
        print(f"Student {self.name} destroyed.")


class Result(Student):
    def __init__(self, name, age, student_id, marks):
        super().__init__(name, age, student_id)
        self.marks = marks
        print(f"Result for {self.name} created.")

    def calculate_highest_lowest(self):
        highest = max(self.marks)
        lowest = min(self.marks)
        print(f"Highest Marks: {highest}, Lowest Marks: {lowest}")

    def display_details(self):
        super().display_details()
        self.calculate_highest_lowest()

    def __del__(self):
        print(f"Result for {self.name} destroyed.")


class HonorsResult(Result):
    def __init__(self, name, age, student_id, marks, classification):
        super().__init__(name, age, student_id, marks)
        self.classification = classification
        print(f"Honors Result for {self.name} created.")

    def display_honors_classification(self):
        average_marks = sum(self.marks) / len(self.marks)
        print(f"Honors Classification: {self.classification}")
        print(f"Average Marks: {average_marks}")
        if average_marks >= 70:
            print(f"{self.name} qualifies for Honors.")
        else:
            print(f"{self.name} does not qualify for Honors.")

    def display_details(self):
        super().display_details()
        self.display_honors_classification()

    def __del__(self):
        print(f"Honors Result for {self.name} destroyed.")



if __name__ == "__main__":
    student1 = HonorsResult("Alice", 20, "S123", [85, 78, 92, 88], "First Class")

    student1.display_details()

    del student1
