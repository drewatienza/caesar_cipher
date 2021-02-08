from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text_input, shift_amount, cipher_direction):
    end_text = ''
    for letter in text_input:
        if cipher_direction == 'encode':
            if letter not in alphabet:
                end_text += letter
            else:
                shift_index = alphabet.index(letter) + shift_amount
                if shift_index > 25:
                    end_text += alphabet[shift_index - 26]
                else:
                    end_text += alphabet[shift_index]
        else:
            if letter not in alphabet:
                end_text += letter
            else:
                shift_index = alphabet.index(letter) - shift_amount
                if shift_index < 0:
                    end_text += alphabet[shift_index + 26]
                else:
                    end_text += alphabet[shift_index]
    print(f'The {cipher_direction}d text is {end_text}.')


encode_decode = True
continue_cipher = True

while continue_cipher:
    while encode_decode:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction == 'encode' or direction == 'decode':
            encode_decode = False
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 25:
        shift = shift % 26

    caesar(text, shift, direction)

    restart = input('Do you want to go again?  Type "yes" or "no".\n')
    if restart == 'no':
        continue_cipher = False
        print('Goodbye')


