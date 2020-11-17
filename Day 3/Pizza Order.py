print("Please order your Pizza")

size = input("What size Pizza do you want? S, M, L")
add_pepperoni = input("Add pepperoni? Y or No")
extra_cheese = input("Extra cheese? Y or N ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill +=20
elif size == "L":
    bill = 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your bill is {bill}")
