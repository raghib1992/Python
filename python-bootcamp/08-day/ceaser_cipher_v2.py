alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(text, shift, direction):
    output_text = ""
    for letter in text:
        if direction.lower() == 'decode':
            shift *= -1
        position = alphabet.index(letter) + shift
        position %= len(alphabet)
        output_text += alphabet[position]
    print(f"Your {direction.lower()} text is: {output_text}")

ceaser(text,shift,direction)