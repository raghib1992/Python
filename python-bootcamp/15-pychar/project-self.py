# Project Description
# 3 hot flavour 1. Espresso(water 50ml, 18g coffee, rate 1.50$) 2. latte (water 200ml, 24g coffee, 150ml milk, 2.50$) 3. cappuccino (water 250ml, 24g coffee, 100ml milk,3.00$)
# starting resource water 300ml, Milk 200ml, Coffee 100g
# coin operate (penny=0.01,Nickel=0.05,Dime=0.10$, quarter=0.25$)

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

# TODO print report (print the available resources)
# TODO Check resources sufficient?
# TODO Process coin
# TODO Check Transaction successful
# TODO Make Coffee


repeat = False

while not repeat:
    if resources["water"] < 50 or resources["coffee"] < 18:
        repeat = True
    ask = input("what would you like/(Espresso/Latte/Cappuccino/): ").lower()

    if ask == 'report':
        print(resources)
        print(profit)
    elif ask == 'espresso':
        required_resource = {"water": 50, "coffee": 18}
        if resources["water"] >= required_resource["water"] and resources["coffee"] >= required_resource["coffee"]:
            print("Please insert $1.50 coins")
            quarters = int(input("How many quarters?: "))*0.25
            print(quarters)
            dimes    = int(input("How many dimes?: "))*0.10
            print(dimes)
            nickles  = int(input("How many nickles?: "))*0.05
            print(nickles)
            pennies  = int(input("How many pennies?: "))*0.01
            print(pennies)
            money    = round(quarters+dimes+nickles+pennies,2)
            profit += 1.5
            print(money)
            if money >=  1.50:
                print(f"Your Espresso is ready ☕.\nBalance amount {money-1.50} is refund")
            else:
                print(f"Insufficient Money.\nNeed to pay more {1.50-money}")
            resources["water"] = resources["water"] - 50
            resources["coffee"] = resources["coffee"] - 18
        else:
            print("Insufficient Resources")
    elif ask == 'latte':
        required_resource = {"water": 200, "coffee": 24, "milk": 150}
        if resources["water"] >= required_resource["water"] and resources["coffee"] >= required_resource["coffee"] and resources["milk"] >= required_resource["milk"]:
            print("Please insert $2.50 coins")
            quarters = int(input("How many quarters?: "))*0.25
            print(quarters)
            dimes    = int(input("How many dimes?: "))*0.10
            print(dimes)
            nickles  = int(input("How many nickles?: "))*0.05
            print(nickles)
            pennies  = int(input("How many pennies?: "))*0.01
            print(pennies)
            money    = round(quarters+dimes+nickles+pennies,2)
            profit += 2.5
            print(money)
            if money >=  2.50:
                print(f"Your Latte is ready ☕\nBalance amount {money-2.50} is refund")
            else:
                print(f"Insufficient Money.\nNeed to pay more {2.50-money}")
            resources["water"] = resources["water"] - 200
            resources["coffee"] = resources["coffee"] - 24
            resources["milk"] = resources["milk"] - 150
        else:
            print("Insufficient Resources")
    elif ask == 'cappuccino':
        required_resource = {"water": 250, "coffee": 24, "milk": 100}
        if resources["water"] >= required_resource["water"] and resources["coffee"] >= required_resource["coffee"] and resources["milk"] >= required_resource["milk"]:
            print("Please insert $3.00 coins")
            quarters = int(input("How many quarters?: "))*0.25
            print(quarters)
            dimes    = int(input("How many dimes?: "))*0.10
            print(dimes)
            nickles  = int(input("How many nickles?: "))*0.05
            print(nickles)
            pennies  = int(input("How many pennies?: "))*0.01
            print(pennies)
            money    = round(quarters+dimes+nickles+pennies,2)
            profit += 3.0
            print(money)    
            if money >=  3.00:
                print(f"Your cappuccino is ready ☕.\nBalance amount {money-1.50} is refund")
            else:
                print(f"Insufficient Money {money}.\nNeed to pay more {3.00-money}")
            resources["water"] = resources["water"] - 250
            resources["coffee"] = resources["coffee"] - 24
            resources["milk"] = resources["milk"] - 100
        else:
            print("Insufficient Resources")
    else:
        repeat = True