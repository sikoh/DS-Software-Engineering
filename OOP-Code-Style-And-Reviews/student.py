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
    names = [
    "Emily", "Liam", "Olivia", "Noah", "Ava", "Ethan", "Sophia", "Jackson", 
    "Emma", "Aiden", "Isabella", "Lucas", "Mia", "Oliver", "Harper", "Elijah", 
    "Amelia", "Logan", "Abigail", "Caleb", "Grace", "Benjamin", "Charlotte", 
    "Henry", "Lily", "Samuel", "Scarlett", "Mason", "Zoe", "Alexander"]
    
    majors = [
    "Computer Science", "Biology", "Psychology", "Engineering", "Business Administration",
    "Environmental Science", "Political Science", "Economics", "English Literature", "Mathematics",
    "Chemistry", "Physics", "History", "Sociology", "Communications",
    "Nursing", "Graphic Design", "Marketing", "Philosophy", "Education",
    "Criminal Justice", "Art History", "Anthropology", "Geology", "International Relations",
    "Music", "Film Studies", "Public Health", "Theater", "Astronomy"]

    students = []
    for i in range(30):
        name = names[i]
        age = random.randint(18, 45)
        major = majors[i]

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
