print("Welcome to treasure island")
print("Your mission is to find treasure")

choice1 = input('There is a fork in the road do you go "Left" or "Right"').lower()


if choice1 == "left":
    choice2 = input('There is a lake. There is an island in the middle. Type "Wait" to wait for a boat or type "Swim" to swim across.').lower()
    if choice2 == "wait":
        choice3 = input("There are three doors, Red Yellow and Blue. Type the colour to use the door").lower()
        if choice3 == "yellow":
            print("You WIn")
        elif choice3 == "red":
            print("Game Over room full of fire")
        elif choice3 == "blue":
            print("Game over you drowned")
    else:
        print("Game Over")
else:
    print("Game over")

