alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(plain_text, shift_amount, direction):
    if direction == "encode":
        encoded_words = ""
        for word in plain_text:
            number = alphabet.index(word)
            if (number+shift_amount) <= 25:
                encoded_words += alphabet[number + shift_amount]
            else:
                encoded_words += alphabet[(number+shift)- 26]
        
        print(f"The encoded text is {encoded_words}")
    else:
        decoded_word = ""
        for letter in plain_text:
            number = alphabet.index(letter)
            if number-shift_amount >= 0:
                decoded_word += alphabet[number - shift_amount]
            else:
                decoded_word += alphabet[26 - (shift_amount-number)]
        
        print(f"The decoded word is {decoded_word}")


ceaser(plain_text=text, shift_amount=shift,direction=direction)