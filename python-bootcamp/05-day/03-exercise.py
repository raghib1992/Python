# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:


# print(list(range(0,101,2)))

total_sum = 0
for n in range(0,101):
    if n % 2 == 0:
        total_sum += n
print(total_sum)

