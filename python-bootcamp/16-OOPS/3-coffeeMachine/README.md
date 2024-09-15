from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



# report = Menu().get_items()
# print(f"List of items available are: {report}")

# resources = CoffeeMaker().report()
# # print(f"Resources avialable are: {resources}")

# order_name = input("what would you like?: ")

# drink = Menu().find_drink(order_name)
# check = CoffeeMaker().is_resource_sufficient(drink)

# if check:
#     prize = MenuItem().cost
#     print(prize)
#     # profit = MoneyMachine().makepayment(money)
    
# Step 1: Create object money_amchine form class MoneyMachine()
money_machine = MoneyMachine()

# Step 2. Using my object money_machine. create report
money_machine.report()

# Step 3: Create second object coffee_maker using class CoffeeMaker()
coffee_maker = CoffeeMaker()
coffee_maker.report()

# Step 4: Create third object item from MenuItem()
## Check sufficient report
menu = Menu()
option = menu.get_items()
order_name = input(f"What would you like? ({option}): ")
drink = menu.find_drink(order_name)
print(coffee_maker.is_resource_sufficient(drink))

#step 5: process payment
money = money_machine.make_payment(drink.cost)
 
