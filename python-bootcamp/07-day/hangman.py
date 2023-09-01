import random
import hangman_art
from hangman_words import word_list
# from replit import clear
import os


print(hangman_art.logo)

# A list od word
# word_list = ["cat", "ball", "pen"]

# variable lives to keep track of the number of lives left
lives = 6
print(hangman_art.stages[6])

# Chose random word from above list
chosen_word = list(random.choice(word_list))
print(chosen_word)

# Creat a empty list as many as elemant as element
display = []
for _ in range(0,len(chosen_word)):
    display.append("_")
print(display)

# Run a loop till user guess all the word
end_of_game = False
while not end_of_game:
    # Ask user to guess a letter
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print("You already guessed this letter")

    # Loop through each position if letter match then reveal the letter
    index = 0
    for letter in chosen_word:
        if letter == guess:
            display[index] = letter            
        index += 1
        
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Won")

    
    
    if guess not in chosen_word:
        lives -= 1
        print(hangman_art.stages[lives])
    
    if lives == 0:
        print("You Lose the game")
        break
    
    # # Clearing the Screen
    # os.system('cls')