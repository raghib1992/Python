alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text,shift):
    letters = list()
    for letter in text:
        position = alphabet.index(letter)
        if shift > 26:
            shift = shift % 26
        position += shift
        if position >= 26:
            new_position = position - 26
            letters.append(alphabet[new_position])
        else:
            letters.append(alphabet[position])
    code = "".join(letters)
    print(code)
    return code

def decrypt(code,shift):
    letters = list()
    for letter in code:
        position = alphabet.index(letter)
        position -= shift
        letters.append(alphabet[position])
    text = "".join(letters)
    print(text)
    return text


code = encrypt(text,shift)
decrypt(code,shift)