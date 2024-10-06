

x = 0
new_number = []
numbers = [11,17,9,3,4,5,6,7,8,5,3,4,5,56,8,8,9,22,45]
print(len(numbers))
while len(numbers) != 0:
    num = 0
    for n in numbers:
        if n >= num:
            num = n
    # print(type(num))
    new_number.append(num)
    x += 1
    # print(numbers)
    numbers.remove(num)
# print(numbers)
print(new_number[::-1])
print(len(new_number))