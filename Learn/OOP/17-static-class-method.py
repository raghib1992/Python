# all method inside a class which used object as first parameter are called instance method

class ClassTest:
    def instance_method(self):
        print(f"called instance method of {self}")
    
test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)

# Class method use different parameter instead of instance(object)
class ClassTest:
    @classmethod
    def class_method(cls):
        print(f"called class_method of {cls}")


# no need to pass any instance in the method, python is samrt enough to pass class in the method
ClassTest.class_method()


# Static method - don't have any parameter. it not really a method, it is a function inside a class
class ClassTest:
    @staticmethod
    def static_method():
        print(f"called staic_method")


ClassTest.static_method()
