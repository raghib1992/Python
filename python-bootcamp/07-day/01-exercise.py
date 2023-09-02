import random

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = list(random.choice(word_list))

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess_word =""
for space in chosen_word:
    guess_word += "_"
print(f"Your word is: \"{guess_word}\"")

# print(user_guess)

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
new_word=list(guess_word)
print(new_word)


end_of_game = False

while not end_of_game:
    
    user_guess = input("Guess the letter: ").lower()
    for l in chosen_word:
        index = 0
        if user_guess == l:
            new_word[index] = l
            print(new_word)
            index += 1
    if '_' not in new_word:
        end_of_game = True
        print("You won")

print(new_word)
# print((''.join(new_word)))
