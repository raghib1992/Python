from jinja2 import Environment, FileSystemLoader
import argparse

parser = argparse.ArgumentParser(description="Greeting Hello to User")

# Use the add_argument method to define arguments your script accepts
parser.add_argument("-a", "--name", help="user name")
parser.add_argument("-o", "--old_password", help="old_password")
parser.add_argument("-n", "--new_password", help="password_password")
parser.add_argument("-u", "--milvus_service", help="milvus service name")
args = parser.parse_args()
args = vars(args)
name = args["name"]
print(name)