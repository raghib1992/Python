from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(plain_text, shift_amount, direction):
    if shift_amount > 25:
        shift_amount = shift_amount % 26

    words = ""
    for i in range(len(plain_text)):
        if plain_text[i] in alphabet:
            number = alphabet.index(plain_text[i])
            if direction == "encode":
                if (number+shift_amount) <= 25:
                    words += alphabet[number + shift_amount]
                else:
                    words += alphabet[(number+shift_amount)- 26]
            elif direction == "decode":
                if number-shift_amount >= 0:
                    words += alphabet[number - shift_amount]
                else:
                    words += alphabet[26 - (shift_amount-number)]
        elif plain_text[i] not in alphabet:
            words += plain_text[i]
    print(f"Your {direction} word is {words}")
            
play_again = "y"
while play_again == "y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # direction = "encode"
    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        ceaser(plain_text=text, shift_amount=shift,direction=direction)
        play_again = input("Do you want to play again: (Y or N) \n")
    else:
        print("Wrong direction input provided.\nKinldy provide either \"encode\" or \"decode\"")