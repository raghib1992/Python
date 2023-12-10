"""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""

families = {"Afsa": 2, "Umar": 2, "Innaya": 4}
h = families.keys()
k = list(families.items())
# print(h,type(h))
# print(families.values())
# print(k[0][0],type(k))

for family in families:
    # print(family)
    # print(families)
    print(f"{family}: {families[family]}")
    # print(f"{family} age is {families[family]}")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["brand"])
# Dictionaries cannot have two items with the same key
# Dictionary Length
print(len(thisdict))
# Dict datatypes
print(type(thisdict))

# The dict() Constructor
employee_details = dict(name = "John", age = 36, country = "Norway")
print(employee_details)


# Accessing Items
x = thisdict["model"]
y = thisdict.get("year")
print(x,y)
# Get Keys
x = thisdict.keys()
print(x)

#  Change Dictionary Items
thisdict["year"] = 2018
print(thisdict.values())
# Update Dictionary
thisdict.update({"model": "Volksvagen"})
print(thisdict)
# Adding Items
thisdict["color"] = "red"
print(thisdict)
thisdict.update({"color": "yellow"})
print(thisdict)

# Removing Items
thisdict.pop("model")
print(thisdict)
# The popitem() method removes the last inserted item
thisdict.popitem()
print(thisdict)
#The del keyword removes the item with the specified key name:
del thisdict["brand"]
print(thisdict)

# Loop Dictionary
families = {"Afsa": 2, "Umar": 2, "Innaya": 4}

for family in families:
    print(family)
    print(families[family])

for family in families.values():
    print(family)

for family in families.keys():
    print(family)

for family,age in families.items():
    print(family, age)

# Copy a Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["color"] = "yellow"
mydict = thisdict.copy()
print(mydict)

x = thisdict
print(x)

mydict = dict(thisdict)
print(mydict)

# Nested Dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)
print(myfamily["child2"]["name"])