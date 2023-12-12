#calculator 
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

num1 = int(input("Input your first number: "))
num2 = int(input("Input your Second number: "))

operation = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide
}

for symbol in operation:
    print(symbol)

operation_symbol= input("Seclect from above operator to perform mathematical function: ")
calculation_function = operation[operation_symbol]
first_answer = calculation_function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol= input("Seclect from above operator to perform mathematical function: ")
num3 = int(input("Input your third number: "))
calculation_function = operation[operation_symbol]
print(calculation_function)
second_answer = calculation_function(first_answer, num3)
print(second_answer)
print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")