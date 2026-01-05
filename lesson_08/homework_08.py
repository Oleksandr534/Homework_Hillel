class Student:
    def __init__(self, firstname, lastname, grade_point_average):
      self.firstname = firstname
      self.lastname = lastname
      self.grade_point_average = grade_point_average


    def status_student(self):
        return f"My name is {self.firstname}"

    def new_point(self, new_point_average=0):
       self.grade_point_average = new_point_average

student_1 = Student("Alex", "Kon", 95)

print(student_1.status_student())
print(student_1.new_point())
      