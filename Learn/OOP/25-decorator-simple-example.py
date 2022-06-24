users = {"name": "Shinu", "access_level": "admin"}

def get_admin_password():
    return "1234"


def secure_function(func):
    if users["access_level"] == "admin":
        return func()

get_password = secure_function(get_admin_password)

print(get_password)