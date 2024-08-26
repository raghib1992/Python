import random
from art import logo

cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
play = True

while play:
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if want_to_play.lower() == 'y':
        print(logo)
        your_card = []
        computer_card = list()
        your_sum = 0
        computer_sum = 0

        for x in range(0,2):
            card = random.choice(cards)
            your_sum += card
            your_card.append(card)
            comp = random.choice(cards)
            computer_sum += comp
            computer_card.append(comp)

        print(f"    Your cards: {your_card}, current score: {your_sum}")
        print(f"    Computer's first card: {computer_card[0]}")

        replay = True
        while replay:
            next_card = input("Type 'y' to get another card, 'n' to pass:  ")
            if next_card == 'y':
                new_card = random.choice(cards)
                your_card.append(new_card)
                your_sum += new_card
                if your_sum > 21:
                    break
                else:
                    print(f"    Your final hand: {your_card}, final score: {your_sum}")
                    print(f"    Computer's first card: {computer_card[0]}")

            else:
                replay = False
        print(f"    Your final hand: {your_card}, final score: {your_sum}")
        print(f"    Computer's final hand: {computer_card}, final score: {computer_sum}")
        if your_sum > 21:
            print("You went over.You lose 😭")
        elif computer_sum > 21:
            print("You win 😆")
        elif your_sum > computer_sum:
            print("You win 😆")
        elif your_sum == computer_sum:
            print("Match draw 🤠")
        else:
            print("You lose 😭")
    else:
        print("Game End")
        play = False
