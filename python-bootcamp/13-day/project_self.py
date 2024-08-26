from itertools import repeat

import art
from game_data import data
import random

def generate_comparison_data(data):
    random_data = random.choice(data)
    # print(f"{random_data["name"]}, {random_data["description"]}, from {random_data["country"]}")
    # return f"{random_data["name"]}, {random_data["description"]}, from {random_data["country"]}"
    return random_data

def comparison(a,b):
    if a > b:
        return 'a'
    else:
        return 'b'

step = 0
repeat = True

while repeat:
    print(art.logo)
    first_data = generate_comparison_data(data)
    print(first_data)
    print(f"Compare A: {first_data["name"]}, {first_data["description"]}, from {first_data["country"]}")
    print(art.vs)
    second_data = generate_comparison_data(data)
    print(second_data)
    print(f"Compare A: {second_data["name"]}, {second_data["description"]}, from {second_data["country"]}")
    winner = comparison(first_data['follower_count'], second_data['follower_count'])
    print(winner)
    user_input = input("Who has more followers? Type 'A' or 'B':  ")
    if user_input.lower() == winner:
        step += 1
        print(f"You're right! Current score: {step}")
    else:
        print(f"Sorry, that's wrong. Final score: {step}")
        repeat = False
