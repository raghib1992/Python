num = list(range(0,11))
print(num)

squ = []
for n in num: 
    a = n**2
    squ.append(a)

print(squ)


sqr = [x**2 for x in range(10,21)]
print(sqr)
################################
num = list(range(0,11))
ev = []
for x in num:
    if x%2 == 0:
        ev.append(x)
print(ev)

od = [x for x in range(0,11) if x % 2 != 0]
print(od)
###############################

# fahrenheit = input("Enter the value of temp in farh: ")
# f = float(fahrenheit)
# degree = (f-32)*(5/9)
# print(f"The value of temp in celcius degree is {degree} degree")




deg = [100, 200, 300]
fah = [(d*(9/5) + 5) for d in deg]
print(fah)

#############################
print(squ)
sqq = [x**2 for x in [x** 2 for x in range(0,11)]]
print(sqq)