# Data Types

# string
"Hello"
## To get the any character from string. This method is caled subscripting
print("Hello"[0])
print("123" + "456")

#Integer
print(123 + 456)

#Float
3.14159

# Boolean
False
True


a = 123
print(type(a))

a = str(123)
print(type(a))


a = float(123)
print(type(a))


print(70 + float("100.75"))


print (str(100) + str(92))

# mathematicals Operator
# PEMDAS LR
print(3 ** 2)
print(5*2)
print(10/2)
print(12+13)
print(15-10)



score = 0
score += 1
print(score)
# round
print(8/3)

print(int(8/3))
print(8//3)
print(type(8//3))

print(round(8/3))
print(round(8/3, 2))


# f-string - to concatenate different data types
score = 128
height = 1.65
isWinning = True
print(f"Your score is {score}, your height is {height}, and you are in winning condition {isWinning}")