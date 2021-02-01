# create option a and b with data from the data file
from game_data import data
import random
from art import logo, vs



# format dictionary into printable data
print(logo)
score = 0
game_not_over = True
option_b = random.choice(data)

def format_data(option):
    account_name = option["name"]
    account_desc = option["description"]
    account_country = option["country"]
    return f"{account_name}, a {account_desc} from {account_country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

while game_not_over:
    option_a = option_b
    option_b = random.choice(data)

    while option_a == option_b:
        option_b = random.choice(data)



    print(f"Compare A: {format_data(option_a)}")
    print(vs)
    print(f"With B: {format_data(option_b)}")
    # ask the user to compare the two option

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # get follower count
    a_follower_count = option_a["follower_count"]
    b_follower_count = option_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry that is wrong. Your final score was {score}.")
        game_not_over = False