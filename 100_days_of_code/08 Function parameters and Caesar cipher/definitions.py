
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_ammount):
    ''' shift the alphabet forward to encrypt the word '''
    
    if shift_ammount > 26:
        shift_ammount = shift_ammount % 26
    
    # empty string to store encrypted letters
    encrypted = ''
    
    #loop through every letter in plain_text
    for letter in plain_text:
        if letter in alphabet:
            # get index position
            position = alphabet.index(letter)
            # get shifted position by adding shift_ammount to positon
            shifted = position + shift_ammount
            # append shifted letters to empty string
            encrypted += alphabet[shifted]
        else:
            encrypted += letter

    return encrypted


def decrypt(encrypted_text, shift_ammount):
    ''' shift the alphabet backwards to decrypt '''
    
    if shift_ammount > 26:
        shift_ammount = shift_ammount % 26
    
    decrypted = ''

    for letter in encrypted_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            shifted = position - shift_ammount
            decrypted += alphabet[shifted]
        else:
            decrypted += letter

    return decrypted


def caesar(input_text, shift_ammount, direction):
    ''' combine encrypt and decrypt functions in to single function '''
    
    if shift_ammount > 26:
        shift_ammount = shift_ammount % 26
    
    output_text = ''

    for letter in input_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == 'encode':
                shifted = position + shift_ammount
                output_text += alphabet[shifted]
            elif direction == 'decode':
                shifted = position - shift_ammount
                output_text += alphabet[shifted]
        else:
            output_text += letter

    return output_text
