alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text,shift):
    # Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter) + shift
        position %= len(alphabet)
        cipher_text += alphabet[position]
    print(f"The encoded text is {cipher_text}")
    return cipher_text

# Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text,shift):
    # Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text
    output_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter) - shift
        position %= len(alphabet)
        output_text += alphabet[position]
    print(f"Here is the encoded result: {output_text}")

code = encrypt(text,shift)
decrypt(code,shift)
