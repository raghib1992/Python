class Student:
    def __inti__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("Raghib", (71, 95, 69, 44))

print(student.name)