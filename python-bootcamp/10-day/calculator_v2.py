from art import logo



def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():
    print(logo)
    
    ops = {
        '+' : add,
        '-' : sub,
        '*' : multiply,
        '/' : divide,  
    }

    first_number = int(input ("What's your first number: "))

    keep_calcualting = True

    while keep_calcualting:
        for key,value in ops.items():
            print(key)
        operator = input("pick an operation: ")
        second_number = int(input ("What's your second number: "))
        
        ops_function = ops[operator]
        cal_result = ops_function(first_number, second_number)
        print(f"{first_number} {operator} {second_number} = {cal_result}")
        want_to_cal = input("Wants to continue the calculation: 'y' or 'n' ")
        if want_to_cal == 'n':
            keep_calcualting = False
            calculator()
        else:
            first_number = float(cal_result)

calculator()