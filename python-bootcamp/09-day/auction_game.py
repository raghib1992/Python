import art

print(art.logo)

auction = {}
def auction_game(biders, amount):
    key = biders
    auction[key] = amount


want_to_bid = 'y'

while want_to_bid == "y":
    user = input("What is the bidder name: ")
    bid_amount = int(input("What is the bid amount: "))
    auction_game(biders=user,amount=bid_amount)
    want_to_bid = input("Want to bid again: 'y' or 'n'")


# print(auction)
a = 0
winner = ""
for key, value in auction.items():
    if value > a:
        a = value
        winner = key

print(f"Highest bidder is {winner}")