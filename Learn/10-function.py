from ast import Pass


def hello():
    print("Hello!")

hello()

def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print (f"Your age in second is {age_seconds}.")

user_age_in_seconds()
#################

def add(x,y):
    result = x+y
    print(result)

add (3,5)
####################
# Default value
def add(x,y=9):
    result = x+y
    print(result)

add (3,5)
########################################





