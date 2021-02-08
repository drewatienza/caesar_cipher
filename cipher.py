alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

encode_decode = True

while encode_decode:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == 'encode' or direction == 'decode':
        encode_decode = False
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text_input, shift_amount, cipher_direction):
    end_text = ''
    for letter in text_input:
        if cipher_direction == 'encode':
            shift_index = alphabet.index(letter) + shift_amount
            if shift_index > 25:
                end_text += alphabet[shift_index - 26]
            else:
                end_text += alphabet[shift_index]
        else:
            shift_index = alphabet.index(letter) - shift_amount
            if shift_index < 0:
                end_text += alphabet[shift_index + 26]
            else:
                end_text += alphabet[shift_index]
    print(f'The encoded text is {end_text}.')


caesar(text, shift, direction)
