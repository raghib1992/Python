alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text,shift):
    # Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    words = list(text)
    encoded_words =[]
    for word in words:
        number = alphabet.index(word)
        if (number+shift) <= 25:
            number += shift
            encoded_words.append(alphabet[number])
        else:
            new_number = 26-(number+shift)
            encoded_words.append(alphabet[new_number])
        
        encoded_text = ''.join(encoded_words)
    
    print(f"The encoded text is {encoded_text}")

# Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(decoded_text,shift_amount):
    # Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text
    encrypted_word = ""
    for letter in decoded_text:
        number = alphabet.index(letter)
        if number-shift_amount >= 0:
            encrypted_word += alphabet[number - shift_amount]
        else:
            encrypted_word += alphabet[26 - (shift_amount-number)]
    
    print(f"The decoded word is {encrypted_word}")

# Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
if direction == "encode":
    encrypt(text,shift)
else:
    decrypt(decoded_text=text,shift_amount=shift)