# recursion


def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


def calculation():
    num1 = int(input("Input your first number: "))

    should_continue = True
    while should_continue:
        operation = {
            "+": add,
            "-": sub,
            "*": multiply,
            "/": divide
        }
        for symbol in operation:
            print(symbol)
        operation_symbol= input("Seclect from above operator to perform mathematical function: ")
        num2 = int(input("Input your Next number: "))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        cal = input("If you want to continue calculation press \"Y/y\", restart press \"R/r\" or press \"N/n\" to exit: ")
        print(cal)
        if cal == "y":
            num1 = answer
        elif cal == "r":
            calculation()
        else:
            should_continue = False
            print("Exit from Calculator")

calculation()