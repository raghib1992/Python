play = True
bidding = dict()
num = 0
winner = ""
while play:
    name = input("What is your name?\n")
    bid = int(input("what is your bid amount?\n"))
    bidding[name] = bid
    
    restart = input("More bidder want to bid: (Y/y or N/n)\n")
    if bid > num:
        num = bid
        winner = name
    else:
        pass
    if restart.lower() == 'n':
        play = False

print(f"Winner of this e auction is: {winner}")