import kubernetes
from kubernetes import client, config
from jinja2 import Environment, FileSystemLoader
import yaml

config.load_kube_config()
core_v1 = client.CoreV1Api()

# List of namesopace
namespace = ['brown-dev-001']

def get_pvc_details(namespace):
    print(namespace)
    pvc = core_v1.list_persistent_volume_claim_for_all_namespaces()
    pvc_list = list()
    for item in pvc.items:
        pvc_details = {}
        if item.metadata.namespace in namespace:
            if item.spec.access_modes[0] == 'ReadWriteMany':
                pvc_details['metadata'] = {}
                pvc_details['metadata']['name'] = item.metadata.name
                pvc_details['metadata']['namespace'] = item.metadata.namespace
                pvc_details['spec'] = {}
                pvc_details['spec']['resources'] = {}
                pvc_details['spec']['resources']['requests'] = {}
                pvc_details['spec']['resources']['requests']['storage'] = item.spec.resources.requests['storage']
                pvc_details['spec']['storageClassName'] = item.spec.storage_class_name
                pvc_details['spec']['volumeMode'] = item.spec.volume_mode
                pvc_details['spec']['volumeName'] = item.spec.volume_name
                pvc_list.append(pvc_details)
    print(pvc_list)
    return pvc_list

def create_pvc_manifest(data):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('pvc_template.yaml.j2')
    # for pvc in data:
    # print(pvc['metadata']['name'])
    # filename = f"output/pvc_{pvc['metadata']['namespace']}.yaml"
    filename = "output/pvc_brown_dev_001.yaml"
    print(filename)
    rendered_yaml = template.render(all_claims=data)
    with open(filename, "w") as f:
        f.write(rendered_yaml)
    print(f"YAML file {filename} generated successfully.")


data = [
    {'metadata': {'name': 'datavol-openvaccine-dataset', 'namespace': 'brown-dev-001'}, 'spec': {'resources': {'requests': {'storage': '10Gi'}}, 'storageClassName': 'ontap-silver', 'volumeMode': 'Filesystem', 'volumeName': 'pvc-2051e61c-b63f-4039-a0ce-e1a43d623de8'}}, 
    {'metadata': {'name': 'shared-brown-dev-001', 'namespace': 'brown-dev-001'}, 'spec': {'resources': {'requests': {'storage': '4Gi'}}, 'storageClassName': 'fsx-ontap-silver', 'volumeMode': 'Filesystem', 'volumeName': 'pvc-8bac86ff-d59e-44c2-bdee-25b7d501e1de'}}
    ]

# data = get_pvc_details(namespace)
create_pvc_manifest(data)