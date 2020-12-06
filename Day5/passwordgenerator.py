import random

#Password Generator Project

list_of_letters = []
list_of_numbers = []
list_of_symbols = []
all_characters = []
randomised_password = ''

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for nr_letters in range(1, nr_letters +1):
    list_of_letters += random.choice(letters)

for nr_symbols in range(1, nr_symbols + 1):
    list_of_symbols += random.choice(symbols)

for nr_numbers in range(1, nr_numbers + 1):
    list_of_numbers += random.choice(numbers)

all_characters = list_of_letters + list_of_numbers + list_of_symbols
random.shuffle(all_characters)
randomised_password = ''.join(all_characters)


print(randomised_password)
