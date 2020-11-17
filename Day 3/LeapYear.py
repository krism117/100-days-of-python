

year = int(input("Which year would you like to check? "))



if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")