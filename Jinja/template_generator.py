import yaml
from jinja2 import Environment, FileSystemLoader

# import json

# # Load JSON data
# with open('pipeline.json') as f:
#     data = json.load(f)

# # Jinja2 template
# with open('template.j2', 'r') as template_file:
#     template = template_file.read()

# # Render the template
# jinja_env = jinja2.Environment(loader=jinja2.BaseLoader())
# rendered_template = jinja_env.from_string(template).render(data=data)

# # Save the rendered template to a file
# with open('output.yaml', 'w') as f:
#     f.write(rendered_template)

with open('value.yaml','r') as read_file:
    values = yaml.safe_load(read_file)
    print(list(values))

# Load templates file from templtes folder
env = Environment(loader = FileSystemLoader('./'))
template = env.get_template('compoment_tmpl.j2')

for service in values["services"]:
    file=open("output/SVC-"+service['name']+".yaml", "w")
    file.write(template.render(service))
    file.close()
