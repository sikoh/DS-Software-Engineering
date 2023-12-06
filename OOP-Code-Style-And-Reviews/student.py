import random

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print(f"{self.name} is studying.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class BloomTechStudent(Student):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def attend_bloomtech_event(self):
        print(f"{self.name} is attending a BloomTech event for {self.major} majors.")

def student_generator():
    names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Harry", "Ivy", "Jack"]
    majors = ["Computer Science", "Engineering", "Business", "Biology", "Psychology", "Mathematics"]

    students = []
    for i in range(30):
        name = random.choice(names)
        age = random.randint(18, 45)
        major = random.choice(majors)

        student = BloomTechStudent(name, age, major)
        students.append(student)

    return students

if __name__ == "__main__":
    # Generate 30 BloomTech students
    bloomtech_students = student_generator()

    # Example usage
    for student in bloomtech_students:
        student.study()
        student.attend_bloomtech_event()
        print(f"{student.name} is {student.age} years old and is majoring in {student.major}.")
        print("-" * 30)