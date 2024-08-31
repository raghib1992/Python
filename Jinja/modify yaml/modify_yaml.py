import yaml

# Load the existing YAML file
with open('config.yaml', 'r') as file:
    existing_config = yaml.safe_load(file)
    
print(existing_config)

new_content = {
    'services': {
        'db': {
            'image': 'mysql:13',
            'ports': ['3306:3306']
        }
    }
}

if 'services' in existing_config:
    existing_config['services'].update(new_content['services'])
else:
    existing_config['services'] = new_content['services']
    
print(existing_config)

with open('config.yaml', 'w') as file:
    yaml.safe_dump(existing_config, file)

