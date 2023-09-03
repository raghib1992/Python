from art import logo

print(logo)

first_number = int(input ("What's your first number: "))
print("+\n-\n*\n/")

def add(first_number, second_number):
    return first_number + second_number

def sub(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    return first_number * second_number

def divide(first_number, second_number):
    return first_number/second_number

def calcualtion(first_number, second_number, operator):
    ops = {
        '+' : add(first_number, second_number),
        '-' : sub(first_number, second_number),
        '*' : multiply(first_number, second_number),
        '/' : divide(first_number, second_number),  
    }
    result = ops[operator]
    return f"{result}"


keep_calcualting = True

while keep_calcualting:
    operator = input("pick an operation: ")
    second_number = int(input ("What's your second number: "))
    cal_result = calcualtion(first_number, second_number, operator)
    print(f"{first_number} {operator} {second_number} = {cal_result}")
    want_to_cal = input("Wants to continue the calculation: 'y' or 'n' ")
    if want_to_cal == 'n':
        keep_calcualting = False
    else:
        first_number = float(cal_result)