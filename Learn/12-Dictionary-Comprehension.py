users = [
    (0, "bob", "password"),
    (1, "rolf", "rolf123"),
    (2, "Jose", "Long4assword"),
    (3, "username", "1234")
]

username_mapping = {user[1]: user for user in users}

print(username_mapping["bob"])

username_input = input("Enter Your Username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct")
else:
    print("Your details are incorrect")