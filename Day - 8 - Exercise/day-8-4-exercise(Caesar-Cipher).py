import os
import time
import art
import loading

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d result is: {end_text}")


for i in range(1):
    print("\n\n", loading.load_logo1)
    time.sleep(1.8)
    os.system('cls')

    print("\n\n\n\n", loading.load_logo2)
    time.sleep(1.8)
    os.system('cls')

    print("\n\n\n\n\n\n", loading.load_logo3)
    time.sleep(1.8)
    os.system('cls')

    print("\n\n\n\n\n\n\n\n", loading.load_logo4)
    time.sleep(1.8)
    os.system('cls')

print("\n\n\n\n\n\n\n\n\n", loading.load_done_logo)
time.sleep(1.2)
os.system('cls')


print(art.logo)

end_cipher = False
while not end_cipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'Yes' if you want to go again. Otherwise type 'No'.\n").lower()
    if restart == "no":
        end_cipher = True
        os.system('cls')
        print(art.end_logo)
        time.sleep(2)
        print(art.bye)
        time.sleep(4)
        os.system('cls')
        print("\n\n\n\n\nCLEARING FILES................")
        time.sleep(2)
        os.system('cls')
        print(art.end_logo2)

    elif restart == "yes":
        os.system('cls')
        print(art.logo)

    else:
        print("We didn't Understand that. Please try again...")
        exit()

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         encrypt_letter_position = (position + shift_amount) % 26
#         cipher_text += alphabet[encrypt_letter_position]
#
#     print(f"The encoded text is {cipher_text}")
#
#
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         plain_letter_position = (position - shift_amount) % 26
#         plain_text += alphabet[plain_letter_position]
#
#     print(f"The decoded text is {plain_text}")
#
#
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)