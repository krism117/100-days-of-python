MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def format_data(resources):
    amount_of_water = resources["water"]
    amount_of_milk = resources["milk"]
    amount_of_coffee = resources["coffee"]
    return f"Water: {amount_of_water}\n Milk: {amount_of_milk}\n Coffee: {amount_of_coffee}"


def check_resources(order):
    global resources
    amount_of_water = resources["water"]
    amount_of_coffee = resources["coffee"]
    amount_of_milk = resources["milk"]
    if order == "espresso" and resources["water"] > 50 and resources["coffee"] > 18:
        resources["water"] = amount_of_water - 50
        resources["coffee"] = amount_of_coffee - 18
        return True
    elif order == "latte" and resources["water"] > 200 and resources["coffee"] > 24 and resources["milk"] > 150:
        resources["water"] = amount_of_water - 200
        resources["coffee"] = amount_of_coffee - 24
        resources["milk"] = amount_of_milk - 150
        return True
    elif order == "cappuccino" and resources["water"] > 250 and resources["coffee"] > 24 and resources["milk"] > 100:
        resources["water"] = amount_of_water - 250
        resources["coffee"] = amount_of_coffee - 24
        resources["milk"] = amount_of_milk - 100
        return True

# TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”






# TODO 2. Turn off the Coffee Machine by entering “ off ” to the prompt.

machine_on = True


# TODO 3. Print report.
while machine_on:
    order = ""
    order = input("What would you like? (espresso/latte/cappuccino):").lower()
    if order =="report":
        format_data(resources)
        print(f" {format_data(resources)}")
    elif order == "espresso":
        if check_resources(order):
            amount_paid = float(input("Insert £1.50"))
            if amount_paid == float(1.50):
                print("Here is your coffee!")
        else:
            print("Sorry not enough resources")
    elif order == "latte":
        if check_resources(order):
            amount_paid = float(input("Insert £2.50"))
            if amount_paid == float(2.50):
                print("Here is your coffee!")
        else:
            print("Sorry not enough resources")
    elif order == "cappuccino":
        if check_resources(order):
            amount_paid = float(input("Insert £3.00"))
            if amount_paid == float(3.00):
                print("Here is your coffee!")
        else:
            print("Sorry not enough resources")

    elif order == "off":
        machine_on = False


# TODO 4. Check resources sufficient?






# TODO 5. Process coins.


# TODO 6. Check transaction successful?


# TODO 7. Make Coffee.