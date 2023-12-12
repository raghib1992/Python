import random
# you = []
# dealer = []


# for i in range(1,3):
#     deal = random.randint(1,10)
#     you.append(deal)
# for i in range(1,3):
#     deal = random.randint(1,10)
#     dealer.append(deal)
# print(you)
# print(dealer)  
# if input("You want to hit again type \"y/Y\" or stand type \"N/n\": ").lower() == "y":
#     print("You choose to add card")
#     hit = True
#     while hit:
#         if input("You want to hit again type \"y/Y\" or stand type \"N/n\": ").lower() == "y":
#             deal = random.randint(1,10)
#             you.append(deal)
#             print(you)
#         else:
#             print("You choose to exit")
#             break
# else:
#     print("You chose to exit")
#     you_sum = 0
#     deal_sum = 0
#     for y in you:
#         you_sum += y
#     for d in dealer:
#         deal_sum += d
#     print(you_sum)
#     print(deal_sum)
#     if you_sum > 21:
#         print(f"Your Total is {you_sum}, which is greater than 21. You Loose")
#     elif you_sum > deal_sum:
#         print(f"You win")
#     else:
#         print("You Loose")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    print(cards[random.randint(2,11)])
    return cards[random.randint(2,11)]

user_cards = []
computer_cards = []

deal_card()