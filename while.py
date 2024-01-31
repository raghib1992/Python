
# number = 0

# while number <= 10:
#     print(f"{number}. I Love Uzma")
#     number = number + 1

# i = 1
# while True:
#     if i % 0o7 == 0:
#         break
#     print(i)
#     i += 1

# i = 1
# x = 3
# sum = 0
# while ( i <= x ):
#  print(f"sum = {sum}; before add to i")
#  print(f"i = {i}")
#  sum += i
#  print(f"sum = {sum}; after add to i")
#  i += 1
#  print(f"i = {i}")
# print(sum)

i = 5
while True:
    print(i % 0o11)
    if i % 0o11 == 0:
        print(f"i = {i}")
        print(" print this" + str(i%0o11))
        break
    print(i)
    i += 1