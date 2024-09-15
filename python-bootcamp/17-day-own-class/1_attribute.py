# Creating first class User:
class User:
    pass # do nothing

user_1 = User()
user_1.id = "001"
user_1.username = "Raghib"

print(user_1.id)
print(user_1.username)

user_2 = User()
user_2.id = "002"
user_2.username = "Rashid"

print(user_2.id)
print(user_2.username)

#----------------------------------------------#
# Add attribute inside class using Constructor or initializer 

class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.follower = 0
        
user_1 = User('001', 'Shaheen')
user_2 = User('002', 'Uzma')

print(user_1.id, user_1.username)
print(user_2.id, user_2.username)