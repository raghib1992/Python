lambda x, y: x + y



def double(x):
    return x * 2

sequences = [1,4,6]
# doubled = list(map(double, sequences))
# doubled = [double(x) for x in sequences]
doubled = list(map(lambda x: x * 2, sequences))

print(doubled)

