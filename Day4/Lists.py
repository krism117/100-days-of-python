import random

test_seed = int(input("Seed"))
random.seed(test_seed)

nameAsCSV = input("names ")
names = nameAsCSV.split(", ")

number_guests = len(names)
selected = random.randint(0, number_guests - 1)
who_pays = names[selected]
print(who_pays)