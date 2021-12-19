import machine_data


def calculate_coins(quarters, dimes, nickles, pennies):
    """Returns the amount of money in $ that user inserted. Input is the number of coins user inserted."""
    total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    return total


def print_report():
    """Prints report of total amount of money, milk, coffee and water."""
    print(f"Water {machine_data.resources['water']}ml")
    print(f"Milk {machine_data.resources['milk']}ml")
    print(f"Coffee {machine_data.resources['coffee']}g")
    print(f"Money ${machine_data.resources['money']:.2f}")


def verify_input(user_input, correct_input):
    """Returns True if the user_input is inside correct_input (list) False in other way."""
    if user_input in correct_input:
        return True
    else:
        return False


def verify_resources(water_needed, coffee_needed, milk_needed):
    """Returns True if there is enough water, coffee and milk in machine_data.resources."""

    water_left = machine_data.resources["water"] - water_needed
    coffee_left = machine_data.resources["coffee"] - coffee_needed
    milk_left = machine_data.resources["milk"] - milk_needed
    if water_left > 0 and coffee_left > 0 and milk_left > 0:
        return True
    else:
        return False


def coffee_functionality(coffee_type):
    print("Please insert coins.")
    user_quarters = int(input("How many quarters? "))
    user_dimes = int(input("How many dimes? "))
    user_nickles = int(input("How many nickles? "))
    user_pennies = int(input("How many pennies? "))
    total_user_coins = calculate_coins(user_quarters, user_dimes, user_nickles, user_pennies)

    if total_user_coins < machine_data.MENU[coffee_type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here is ${total_user_coins - machine_data.MENU[coffee_type]['cost']:.2f} in change.")

        machine_data.resources["water"] -= machine_data.MENU[coffee_type]["ingredients"]["water"]
        machine_data.resources["milk"] -= machine_data.MENU[coffee_type]["ingredients"]["milk"]
        machine_data.resources["coffee"] -= machine_data.MENU[coffee_type]["ingredients"]["coffee"]
        machine_data.resources["money"] += total_user_coins

        print(f"Here is your {coffee_type}. Enjoy your beverage.")

is_game_over = False
while not is_game_over:
    user_choice = input("What would you like? (espresso/latte/cappuccino) ").lower()

    if user_choice in ["espresso", "latte", "cappuccino"]:
        coffee_functionality(user_choice)
    elif user_choice == "report":
        print_report()
    elif user_choice == "off":
        is_game_over = True
