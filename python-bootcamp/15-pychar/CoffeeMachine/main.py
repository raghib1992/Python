MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# TODO: Check resources sufficient

def is_resources_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
# TODO: Ask user for Input
is_on = True
while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    # TODO: Turn Off Coffee Machine
    if choice == "off":
        is_on = False
    # TODO: Print Report
    elif choice == "report":
        print(f'Milk: {resources["milk"]} ')
        print(f'Coffee: {resources["coffee"]}')
        print(f'Money: {profit}')
        print(f'Water:{resources["water"]}')
    else:
        drink = MENU[choice]
        print(drink['ingredients'])
        if is_resources_sufficient(drink['ingredients']):




# TODO: Process coins

# TODO: Check transaction successful

# TODO: Make Coffee.
