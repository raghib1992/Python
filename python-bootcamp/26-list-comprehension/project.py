import pandas


#TODO 1. Create a dictionary in this format:
words = pandas.read_csv("nato_phonetic_alphabet.csv")
print(words)
words_dict = { row.letter:row.code for (index,row) in words.iterrows()}
print(words_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_inputs = input("Enter a words: ")
code = [ words_dict[alphabet.upper()] for alphabet in user_inputs]
print(code)