# Thayer Yang
# 02 OCT 2024
# Caesar Cipher

alphabet = 'abcdfeghijklmnopqrstuvwxyz'
new_message = ''

user_message = input('Enter your secret message:\n')
key = int(input('Enter a key: \n'))

for character in user_message:
    if character in alphabet:
        position = alphabet.find(character)
        new_position = (position + key) % 26
        new_character = alphabet[new_position]

        new_message += new_character
    elif character in alphabet.upper():
        upper_alphabet = alphabet.upper()
        position = upper_alphabet.find(character)
        new_position = (position + key) % 26
        new_character = upper_alphabet[new_position]

        new_message += new_character
    else:
        new_message += character

print('Your new message is \n'+ new_message)