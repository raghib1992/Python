import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line

choice = [rock, paper, scissors]
# print(choice[2])
user = int(input("Your input for '0 for Rock', '1 for paper' and '2 for Scissors: "))
computer = print(f"Comper had choose \n {choice[random.randint(0,2)]}")
user_show = computer = print(f"User had choose \n {choice[user]}")

