import yaml


with open('file2.yaml','r') as read_file:
    file2 = read_file.read()
    print(file2)
    
with open('file1.yaml', 'a', newline='') as write_file:
    write_file.write(file2)
    print("updates file1.yaml")