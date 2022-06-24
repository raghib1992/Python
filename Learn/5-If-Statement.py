# If Statement, allow boolean to make decision

# from re import U


day_of_the_week = input("What day of the week is it today? ")
print (day_of_the_week == "Monday")

if day_of_the_week == "Monday":
    # if true than this code will run
    print(f'Have a great start on {day_of_the_week}')
elif day_of_the_week == "Tuesday":
    print(f"Today is {day_of_the_week}")

else:
    print("Full speed ahead")

##########################################

movies_watched = {"Titanic", "Edge Of Tomorrow", "Matrix"}
print(f"Select from this list{movies_watched}")
user_movie = input("Enter something you've watched recently: ")

if user_movie in movies_watched:
    print("I watched user moveis")
else:
    print("I havn't watched that yet")
###############################


