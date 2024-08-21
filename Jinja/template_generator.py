import yaml
from jinja2 import Environment, FileSystemLoader
# import jinja2
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


if __name__ == "__main__":
    values = yaml.load(open('./value.yaml'))
    # Load templates file from templtes folder
    env = Environment(loader = FileSystemLoader('./templates'),   trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('compoment_tmpl.j2')
    for service in values["services"]:
        file=open("resultfile/SVC-"+service['name']+".yaml", "w")
        file.write(template.render(service))
        file.close()
