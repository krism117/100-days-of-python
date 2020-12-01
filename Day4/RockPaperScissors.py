import random

player_choice = input("Type: Rock, Paper or Scissors. ").lower()




rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
computer_choice = random.randint(0, 2)

print("You choose: ")
if player_choice == "rock":
    print(rock)
elif player_choice == "paper":
    print(paper)
elif player_choice == "scissors":
    print(scissors)

print("The computer choose:")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if player_choice == "rock":
    if computer_choice == 0:
        print("It's a draw")
    elif computer_choice ==1:
        print("you loose")
    elif computer_choice == 2:
        print("You win!")
elif player_choice == "paper":
    if computer_choice == 0:
        print("You win")
    elif computer_choice ==1:
        print("It's a draw")
    elif computer_choice == 2:
        print("You loose")
elif player_choice == "scissors":
    if computer_choice == 0:
        print("You loose")
    elif computer_choice ==1:
        print("You win")
    elif computer_choice == 2:
        print("It's a draw")

