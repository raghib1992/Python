# FUnction with output

def capital_name(f_name, l_name):
    last = l_name.upper()
    first = f_name.upper()
    print(first + " " + last)


def title_name(f_name, l_name):
    last = l_name.title()
    first = f_name.title()
    return f"{first} {last}"

capital_name("raghib", "nadim")

output = title_name("raghib", "nadim")
print(output)