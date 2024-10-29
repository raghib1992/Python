# Create a list by adding 1 on each element in list
numbers = [1,2,3,4,5]
new_numbers = [n+1 for n in numbers]
print(new_numbers)



# take a range from 1,5 and create list by double 
new_list = [n*2 for n in range(1,5)]
print(new_list)

# Make uppercase to name lenght equal and greater then 5
names = ["Uzma", "Shaheen", "Raghib", "Nilu", "Neshat", "Ammi", "Papa"]
new_names = [ name.upper() for name in names if len(name) >= 5]
print(new_names)

with open("file1.txt") as file1:
  list1 = file1.readlines()
    
with open("file2.txt") as file2:
  list2 = file2.readlines()
    
result = [int(num) for num in list1 if num in list2]
 
print(result)

with open("file1.txt","r") as file:
    num1=[int(n) for n in file.read().splitlines()]

with open("file2.txt","r") as file:
    num2=[int(n) for n in file.read().splitlines()]

result = [n for n in num1 if n in num2 ]

print(result)
