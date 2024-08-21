import yaml
import jinja2
from jinja2 import Environment, FileSystemLoader

# Read the yaml file and print
with open('value.yaml','r') as read_file:
    contents = yaml.safe_load(read_file)
    print(contents)
    contents["services"].append("Raghib")
    print(contents)


# take the input and generate yaml file
with open('output.yaml','w') as dump_file:
    yaml.dump(contents,dump_file)

# read multiple yaml filw
with open('multiple.yaml','r') as read_file:
    contents = yaml.safe_load_all(read_file)
    print(list(contents))
    print(type(contents))


## everythin in jinja is done through environment
# env = jinja2.Environment()
# template = env.from_string("Hello {{ name }}!")
# output = template.render(name="World")
# print(output)

MAX_SCORE = 100
TEST_NAME = "Python Challenge"

students = [
    {"name" : "Raghib", "score" : 100},
    {"name" : "Uzma", "score" : 89},
    {"name" : "Shaheen", "score" : 77}
]

env = jinja2.Environment(loader=FileSystemLoader("./"))
templates = env.get_template("good.txt")

for student in students:
    name = student["name"]
    filename = f"output/message_{name.lower()}.txt"
    content = templates.render(
        student,
        max_score = MAX_SCORE,
        test_name = TEST_NAME
    )

    with open(filename, mode="w", encoding="utf-8") as output:
        output.write(content)
        print("...wrote",filename)
