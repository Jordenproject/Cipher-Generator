# Welcome text. 
print("Welcome to the Cipher Generator")
print()

# Variable in which the cipher text will be generated from. 
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# User input that will replace any spaces with no spaces and convert any upper case letters to lower. 
user_input = input("Enter a word to be converted into ciphertext: ").replace(" ","").lower()
print()

# Variable that recieves the user key input. 
user_key = input("Enter a key based on your birth month 01 to 12: ")

# If the user enters a character that is not a letter, an exception will be raised. 
if not user_input.isalpha():
    raise ValueError("The word entered must be letters only and no special characters")

# If the user enters a character that is not a number, an exception will be raised. 
if not user_key.isdigit():
    raise ValueError("The key entered must be a number")

# If the user does not enter a number between 1 and 12, an exception will be raised. 
user_key = int(user_key)
if not (1 <= user_key <= 12):
    raise ValueError("The key entered must be between 1 and 12")

# Variable will store a list of characters appended from the for loop. 
result = []

# For each character in user_input, the for loop will move the character along in relation 
# to its position in the alphabet. The number of spaces the character will be moved along will be specified in 
# user_key. 
for char in user_input:

    new_char = (alphabet.index(char) + user_key) % len(alphabet) 
    result.append(alphabet[new_char])
print()

# The new position of each character will be joined together with no spaces and printed out. 
print("Your cipher text is: ",''.join(result))
print()