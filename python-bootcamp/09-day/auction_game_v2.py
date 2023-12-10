from art import logo
import os
clear = lambda: os.system('cls')

print(logo)

bidding_dict = {}
bidding = "yes"

while bidding == "yes":
    name = input("What is your name? ")
    bid = int(input("What is your bid?  $"))

    bidding_dict[name] = bid
    more = input("Is there another user to bid? \"Y\" or \"N\": ").lower()
    if more == "y":
        bidding = "yes"
    else:
        bidding = "no"
    clear()
    
value = 0
winner =""
for bidder in bidding_dict:
    if bidding_dict[bidder] > value:
        value = bidding_dict[bidder]
        winner = bidder

print(f"Winner is {winner}")
