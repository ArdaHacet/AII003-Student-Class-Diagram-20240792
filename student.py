class Student:
    def __init__(self, student_id, name, department):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.gpa = 0.0
        self.courses = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)

    def update_gpa(self, gpa):
        self.gpa = gpa

    def show_info(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("GPA:", self.gpa)
        print("Courses:", self.courses)


student1 = Student("12345", "Ali", "Software Engineering")
student1.add_course("Python")
student1.add_course("Math")
student1.remove_course("Math")
student1.update_gpa(3.2)
student1.show_info()
