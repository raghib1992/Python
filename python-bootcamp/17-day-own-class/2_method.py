class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.follower = 0
        self.following = 0
        
    def follow(self, user):
        user.follower += 1
        self.following +=1
        
user_1 = User('001', 'Shaheen')
user_2 = User('002', 'Uzma')

print(user_1.id, user_1.username)
print(user_2.id, user_2.username)

print(user_1.follower)
user_1.follow(user_2)
print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)