# **CipherGenerator**

## *Overview*
This Python program is a simple Cipher Generator that takes user input in the form of a word and a key (based on the user's birth month). The program will then generate a ciphertext by shifting the letters of the word by a number of positions specified by the key.
## How It Works 
1.	The user enters a word to be converted into ciphertext.
2.	Any spaces in the word are removed, and all letters are converted to lowercase.
3.	The user is prompted to enter a key (a number between 1 and 12, based on their birth month).
4.	The program performs the following checks:
   
    • The word must only contain letters.

    • The key must be a valid number between 1 and 12.

6.	Each letter in the word is shifted along the alphabet by the number specified in the key.
7.	The resulting ciphertext is displayed.

## Example Usage
Here is a sample interaction with the program:
![image](https://github.com/user-attachments/assets/3bbb2545-4078-4bed-ac68-8362e81498c3)

## Requirements

•	Python 3
## Error Handling
The program includes basic error handling:

•	If the word entered contains non-letter characters or spaces, a ValueError will be raised.

•	If the key is not a number or is not between 1 and 12, the program will also raise a ValueError.










