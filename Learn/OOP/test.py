student = {"name": "Omar", "grades": (54, 54, 54)}


class Student():
    def __init__(self,x,y):
        self.name = x
        self.marks = y
    def average(self):
        return sum(self.marks)/len(self.marks)


student1 = Student("Rashid", (95,84,44))
student2 = Student("Raghib", (95,33,44))
print(student2.average())
print(student1.average())