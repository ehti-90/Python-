import string
import random


# Lowercase alphabets
small_letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# Uppercase alphabets
capital_letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# Digits
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Common symbols
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', ';', ':',
    "'", '"', ',', '.', '<', '>', '/', '?', '\\', '|',
    '`', '~'
]

num_of_chars = int(input("How much long character password you want: "))
choice = input("type: easy or difficult : ")


letter = int(input("How many small letters: "))
capital = int(input("How many capital letters: "))
digits = int(input("How many digits letters: "))
symbol = int(input("How many symbols letters: "))

length = letter+capital+digits+symbol

if length != num_of_chars:
    print("Character counts must equal password length.")
    exit()


password = []

if   num_of_chars == length:
    for it in range(letter):
         password.append(random.choice(small_letters))
    for it1 in range(capital):
         password.append(random.choice(capital_letters))
    for it2 in range(digits):
         password.append(random.choice(numbers))
    for it3 in range(symbol):
        password.append(random.choice(symbols))

password_1 =""

if choice == "easy":
    for i in password:
        password_1 += i
    print(password_1)
        
elif choice == "difficult":
    random.shuffle(password)
    for i in password:
        password_1 += i
    print(password_1)
else:
        print("type only choice mentioned")


    


