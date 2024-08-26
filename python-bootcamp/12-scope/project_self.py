import art
import random

print(art.logo)
print("Welcome to the Number Guessing game!")
print("I'm thinking of a number between 1 and 100.")

number = random.choice(list(range(1,101)))
level = input("Choose a difficulty. Type 'easy' or 'hard':  ")

if level == 'easy':
    attempt = 10
else:
    attempt = 5

while attempt >= 1:
    print(f"You have {attempt}  attempts remaining to guess the number.")
    guess = int(input("Make a guess:    "))
    attempt -= 1
    if guess > number:
        print(f"Too high.")
    elif guess < number:
        print(f"Too Low.")
    elif guess == number:
        print(f"You got it 💃! The answer was {guess}")
        break
    if attempt >= 1:
        print("Guess again")
else:
    print("You've run out of guesses, you lose 😭")

