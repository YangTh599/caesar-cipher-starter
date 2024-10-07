# Thayer Yang
# 02 OCT 2024
# Caesar Cipher


def encrypt_message(message,key):
    alphabet = 'abcdfeghijklmnopqrstuvwxyz'
    new_message = ''

    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            new_position = (position + key) % 26
            new_character = alphabet[new_position]

            new_message += new_character   
        else:
            new_message += character

    print('Your encrypted message is \n'+ new_message)
    return new_message

def decrypted_message(message,key):
    alphabet = 'abcdfeghijklmnopqrstuvwxyz'
    new_message = ''

    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]

            new_message += new_character   
        else:
            new_message += character

    print('Your decrypted message is \n'+ new_message)
    return new_message

user_message = input('Enter your secret message:\n').lower()
key = int(input('Enter a key: \n'))

secret = encrypt_message(user_message, key)

not_secret = decrypted_message(secret,key)

print()
print(secret)
print(not_secret)