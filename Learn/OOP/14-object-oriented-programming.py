"""
student = {"Name" : "Raghib", "grades" : (95,69,71,54,63)}

def average(seq):
    return sum(seq)/len(seq)

print(average(student["grades"]))

class Student:
    # A class is a definition of something
    def __init__(self):
        # def how class will behave
        self.name = "Raghib" 
        # taking name property inside of self
        self.grades = (1,2,3,4,5)
    
    def average(marks):
        return sum(marks.grades) / len(marks.grades)

student = Student()
# use the class Student to create a object

print(student.name)
# print the student which is become the self with property name.
print(student.grades)

#################################
class Student:
    # A class is a definition of something
    def __init__(self):
        # def how class will behave
        self.name = "Raghib" 
        # taking name property inside of self
        self.grades = (95,69,71,54,63)
    
    def average(self):
        # defining another method 
        return sum(self.grades) / len(self.grades)


student = Student()

print(student.name, student.grades)
print(Student.average(student))
# print(student.average())
"""
#################
 

class Student():
    def __init__(self, name, marks):
        self.name = name
        self.grades = marks

student= Student("rashid", (1,2,3,4,5))
print(student.name, student.grades)