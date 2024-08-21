from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

def ceaser(plain_text, shift_amount, direction):
    words = ""
    for word in plain_text:
        number = alphabet.index(word)
    
        if direction == "encode":
            if (number+shift_amount) <= 25:
                words += alphabet[number + shift_amount]
            else:
                words += alphabet[(number+shift)- 26]
            # print(f"The encoded text is {words}")
        elif direction == "decode":
            if number-shift_amount >= 0:
                words += alphabet[number - shift_amount]
            else:
                words += alphabet[26 - (shift_amount-number)]
            # print(f"The decoded word is {word}")
    print(f"Your {direction} word is {words}")
            


if direction == "encode" or direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(plain_text=text, shift_amount=shift,direction=direction)
else:
    print("Wrong direction input provided.\nKinldy provide either \"encode\" or \"decode\"")