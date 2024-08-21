from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceaser(text, shift, direction):
    output_text = ""
    for letter in text:
        if direction.lower() == 'decode':
            shift *= -1
        position = alphabet.index(letter) + shift
        position %= len(alphabet)
        output_text += alphabet[position]
    print(f"Your {direction.lower()} text is: {output_text}")

start = True
restart = 'y'
while start:
    if restart == 'y':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        ceaser(text, shift, direction)
        restart = input("Want to restart the programme again, type (Y/y or N/n): ")
    else:
        start = False