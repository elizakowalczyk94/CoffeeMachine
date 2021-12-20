import machine_data


def calculate_coins(quarters, dimes, nickles, pennies):
    """Returns the amount of money in $ that user inserted. Input is the number of coins user inserted."""
    total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    return total


def print_report():
    """Prints report of total amount of money, milk, coffee and water."""
    for ingredient, amount in machine_data.resources.items():
        if amount < 0:
            print(f"{ingredient.capitalize()} 0ml")
        else:
            print(f"{ingredient.capitalize()} {amount}ml")


def verify_input(user_input, correct_input):
    """Returns True if the user_input is inside correct_input (list) False in other way."""
    if user_input in correct_input:
        return True
    else:
        return False


def verify_resources(coffee_ordered):
    """Returns True if there is enough water, coffee and milk in machine_data.resources."""

    water_left = machine_data.resources["water"] - machine_data.MENU[coffee_ordered]["ingredients"]["water"]
    coffee_left = machine_data.resources["coffee"] - machine_data.MENU[coffee_ordered]["ingredients"]["coffee"]
    if coffee_ordered != "espresso":
        milk_left = machine_data.resources["milk"] - machine_data.MENU[coffee_ordered]["ingredients"]["milk"]
        if water_left >= 0 and coffee_left >= 0 and milk_left >= 0:
            return True
    elif coffee_ordered == "espresso":
        if water_left >= 0 and coffee_left >= 0:
            return True
    else:
        return False


def make_coffee(coffee_type):
    print("Please insert coins.")
    user_quarters = int(input("How many quarters? "))
    user_dimes = int(input("How many dimes? "))
    user_nickles = int(input("How many nickles? "))
    user_pennies = int(input("How many pennies? "))
    total_user_coins = calculate_coins(user_quarters, user_dimes, user_nickles, user_pennies)
    user_change = total_user_coins - machine_data.MENU[coffee_type]['cost']

    if total_user_coins < machine_data.MENU[coffee_type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here is ${user_change:.2f} in change.")

        machine_data.resources["water"] -= machine_data.MENU[coffee_type]["ingredients"]["water"]
        machine_data.resources["coffee"] -= machine_data.MENU[coffee_type]["ingredients"]["coffee"]
        if coffee_type != "espresso":
            machine_data.resources["milk"] -= machine_data.MENU[coffee_type]["ingredients"]["milk"]
        machine_data.resources["money"] += (total_user_coins - user_change)

        print(f"Here is your {coffee_type}. Enjoy your beverage.")


is_game_over = False
while not is_game_over:
    user_choice = input("What would you like? (espresso/latte/cappuccino) ").lower()

    if user_choice in ["espresso", "latte", "cappuccino"]:
        if verify_resources(user_choice):
            make_coffee(user_choice)
        else:
            print("Not enough resources.")
    elif user_choice == "report":
        print_report()
    elif user_choice == "off":
        is_game_over = True
        print("Good Bye! See you soon.")
    else:
        print("Wrong input. Try once again.")
