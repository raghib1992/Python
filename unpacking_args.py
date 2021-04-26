def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg
    return(total)

print(multiply(2, 3))

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "NO Valid Operator provided to apply()"

print(apply(2,4,6, operator="*"))