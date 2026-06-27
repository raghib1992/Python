# python Object -Oriented Programming (OOP)


# WHy OOP?
# OOP allows us to structure our software in a particular way. It allows us to create objects that have both data and functionality. This allows us to create more complex and powerful programs.

# Classes and Instances
# A class is a blueprint for creating objects. It defines the properties and methods that an object will have. An instance is a specific object created from a class. It has its own unique data and can use the methods defined in the class.



class Employee:
    pass


emp_1 = Employee()
emp_2 = Employee()


print(emp_1)
print(emp_2)

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_1.pay)

print(emp_2.email)
print(emp_2.pay)


## Setting up variable like this is not ideal. We want to be able to create employees without having to set up all of these variables manually. This is where the __init__ method comes in. The __init__ method is a special method that is called when an instance of a class is created. It allows us to initialize the attributes of the instance. We can use it to set up the attributes of the instance when it is created.    

class Employee:
    # initializer or constructor method
    def __init__(self, first, last, pay):
        # these are instance variables
        self.fname = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.fname, self.last)
    
emp_1 = Employee('Corey', 'Schafer', 50000)

print(emp_1)
print(emp_1.fname)
print(emp_1.last)
print(emp_1.email)
print(emp_1.pay)


print('{} {}'.format(emp_1.fname, emp_1.last))

print(emp_1.fullname())


emp_2 = Employee('Test', 'User', 60000)

print(emp_2.fullname())


print(Employee.fullname(emp_1))
