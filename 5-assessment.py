# class Car():
#     def __init__(self,model) -> None:
#         self.model = model
#         self.name = "Verna"

# like = Car(model="sedan")

# print(like.model)
# print(like.name)
stores = [
    {
        'name': 'My Book Store',
        'items': [
            {
                'name': 'the secret',
                'prize': 379
            }
        ]
    }
]
def get_store(name):
    # iterate over stores
    # If stores matches return it
    # If stores not match, return error
    for store in stores:
        if store['name'] == name:
            print(store)
        else:
           print("Error")

get_store("My Book Store")