# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

digit = input("Type a two digit number: \n")
first_digit = int(digit[0])
second_digit = int(digit[1])
print (f"The sum of two digits are: {first_digit + second_digit}")