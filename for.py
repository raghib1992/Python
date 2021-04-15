x = {1,2,3,4}
for number in x:
    print(f"{number} is the way to show")



shaheen = [35,55,66,78,99]
total=0
subject=len(shaheen)
for marks in shaheen:
    total +=marks    # total = total + marks

print(total/subject)

shaheen = [35,55,66,78,99]
total=sum(shaheen)
subject=len(shaheen)

print(total/subject)