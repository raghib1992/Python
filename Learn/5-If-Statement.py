# If Statement, allow boolean to make decision
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b


a = 37
print(a)
b = int(input("Enter number to Compare with 'a': "))
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Short Hand If
if a > b: print("a is greater than b")

# Short Hand If ... Else
print("A") if a > b else print("B")

Days = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}
day_of_the_week = input("What day of the week is it today? ")
print (day_of_the_week == "Monday")
if day_of_the_week in Days:
    if day_of_the_week == "Monday":
        # if true than this code will run
        print(f'Have a great start on {day_of_the_week}')
    elif day_of_the_week == "Saturday" or day_of_the_week == "Sunday" :
        print(f"Have a great weekends {day_of_the_week}")
    else:
        print("Full speed ahead")
else:
    print("Incorrect day name")
##########################################

movies_watched = {"Titanic", "Edge Of Tomorrow", "Matrix"}
print(type(movies_watched))
print(f"Select from this list{movies_watched}")
user_movie = input("Enter something you've watched recently: ")

if user_movie in movies_watched:
    print("I watched user moveis")
else:
    print("I havn't watched that yet")
###############################


