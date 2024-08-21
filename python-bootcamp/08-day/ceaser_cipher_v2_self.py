alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(text, shift, direction):
    words = ""
    for letter in text:
        if direction.lower() == 'encode':
            position = alphabet.index(letter) + shift
        else:
            position = alphabet.index(letter) - shift
        position %= len(alphabet)
        words += alphabet[position]
    print(f"Your {direction.lower()} text is: {words}")

ceaser(text,shift,direction)