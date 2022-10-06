# If Statement, allow boolean to make decision

# from re import U

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


