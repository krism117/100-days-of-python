print("Welcome to the rollercoster")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoster!")
    age = int(input("What is your age? "))
    if age< 12:
        print("Tickets are £5")
        bill = 5
    elif age <= 18:
        print("Tickets are £7")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Have a free ride")
    else:
        print("Tickets are £12")
        bill = 12

    wants_photo = input("Do you want a photo? Y or N")
    if wants_photo == "Y":
        bill += 3

    print(f"Your bill is {bill}")
else:
    print("Sorry you cannot ride")