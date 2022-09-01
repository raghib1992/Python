def return_42():
    # Complete function here
    return 42  # 'pass' just means "do nothing". Make sure to delete this!

print(return_42())


def Convereter():
    fahrenheit = input("The value of temperature in Fahrenheit: ")
    f = float(fahrenheit)
    degree = (f-32)*5/9
    print(f"The Value of the temp in degree is {degree}")

Convereter()