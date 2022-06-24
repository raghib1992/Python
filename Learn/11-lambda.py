def double(x):
    return x * 2

seq = [1, 3, 5, 9]
doubled = [ double(x) for x in seq ]

doubled = map(double, seq)

#################

doubled = [(lambda x: x*2) (x) for x in seq]
doubled = list(map(lambda x:x *2, seq))

#################