alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text_input, shift_amount):
    encrypted_word = ''
    for letter in text_input:
        shift_index = alphabet.index(letter) + shift_amount
        if shift_index > 25:
            encrypted_word += alphabet[shift_index - 26]
        else:
            encrypted_word += alphabet[shift_index]
    print(f'The encoded text is {encrypted_word}.')


encrypt(text, shift)