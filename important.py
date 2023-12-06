# lower() convert all string into lower case
# .count("t") count number of 't' in the string
t = (("Uzma Akhtar").lower()).count("t")


# List
l = [1,2,3,4,5,6]
print(l)
print(l[0])
print(l[-2])
# print from index 1 to till last
print(l[1:])
# print starting 4 index
print(l[:4])
# grab from index 1 to index except last 1, if there was -2 then except last two index grab all
print(l[1:-1])
print(l[1:4])
#append
l.append(7)
print(l)
# remove
l.remove(3)
print(l)
# pop
l.pop()
print(l)
l.pop(2)
print(l)
l.pop(-2)
print(l)
l.pop()
print(l)
# extend
l.extend([3,4,5,6,7])
print(l)
print(l + l)
a= l+l
# sort
a.sort()
print(a)
# print the length
print(len(l))
# reverse the list
print(l)
l.reverse()
print(l)