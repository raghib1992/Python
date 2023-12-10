import art

print(art.logo)

auction = {}

bidding_finished = False

while not bidding_finished:
    name = input("What is bidder name: ")
    bid_amount = int(input("What is the bid amount: "))
    auction[name] = bid_amount
    want_to_bid = input("Want to bid again: 'y' or 'n'\n")
    if want_to_bid == "n":
        bidding_finished = True


highest_bid = 0
winner = ''

for key in auction:
    prize = auction[key]
    if prize > highest_bid:
        highest_bid = prize
        winner = key

print(f"Highest bidder is {winner}")