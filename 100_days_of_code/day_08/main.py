# https://replit.com/@appbrewery
# Caesar encryption

from art import logo
from definitions import *

print(logo)


while True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        word = encrypt(text, shift)
        print(word)
    elif direction == 'decode':
        word = decrypt(text, shift)
        print(word)

    again = input('quit or continue? ')
    if again == 'quit':
        print('Goodbye!')
        break
    else:
        continue


#tags: encode/decode, encription, caesar cipher