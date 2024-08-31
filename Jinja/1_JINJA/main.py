from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))
templates = env.get_template("good.txt")

first_name = 'raghib'

filename = f"some-name-{first_name.lower()}.txt"
content = templates.render(
    name = first_name,
    score = 1000,
    max_score = 890,
    test_name = "BPSE"
)

with open(filename, 'w') as f:
    f.write(content)