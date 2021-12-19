import machine_data

# TODO: ask user about the order - espresso/latte/cappuccino
coffee_type = input("What would you like? (espresso/latte/cappuccino)")
coffee_data = machine_data.MENU[coffee_type]


# TODO: verify if there are enough resources
def verify_resources(water_needed, coffee_needed, milk_needed):
    """Returns True if there is enough water, coffee and milk in machine_data.resources."""

    water_left = machine_data.resources["water"] - water_needed
    coffee_left = machine_data.resources["coffee"] - coffee_needed
    milk_left = machine_data.resources["milk"] - milk_needed
    if water_left > 0 and coffee_left > 0 and milk_left > 0:
        return True
    else:
        return False


# TODO: ask for coins - quarters 0.25, dimes 0.10, nickles 0.05, pennies 0.01
print("Please insert coins.")
user_quarters = int(input("How many quarters? "))
user_dimes = int(input("How many dimes? "))
user_nickles = int(input("How many nickles? "))
user_pennies = int(input("How many pennies? "))
machine_money = 0
is_game_over = False


# while not is_game_over:

# TODO: verify if there is enough money
def calculate_coins(quarters, dimes, nickles, pennies):
    """Returns the amount of money in $ that user inserted. Input is the number of coins user inserted."""
    total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    return total


print(calculate_coins(user_quarters, user_dimes, user_nickles, user_pennies))
total_user_coins = calculate_coins(user_quarters, user_dimes, user_nickles, user_pennies)

if total_user_coins < machine_data.MENU[coffee_type]["cost"]:
    print("Sorry that's not enough money. Money refunded.")
else:
    print(f"Here is ${total_user_coins - machine_data.MENU[coffee_type]['cost']} in change.")

    # TODO: update report
    machine_data.resources["water"] -= machine_data.MENU[coffee_type]["water"]
    machine_data.resources["milk"] -= machine_data.MENU[coffee_type]["milk"]
    machine_data.resources["coffee"] -= machine_data.MENU[coffee_type]["coffee"]
    machine_money += total_user_coins

    # TODO: prepare coffee
    print(f"Here is your {coffee_type}. Enjoy your beverage.")


# TODO: if input is "report" print amount of water, milk, coffee, money
def print_report():
    """Prints report of total amount of money, milk, coffee and water."""
    print(f"Water {machine_data.resources['water']}ml")
    print(f"Milk {machine_data.resources['milk']}ml")
    print(f"Coffee {machine_data.resources['coffee']}g")
    print(f"Money ${machine_money}")


# TODO: if input is "off" finish game
def input_off():
    is_game_over = True


# TODO: if input not correct finish game/ ask again
def verify_input(user_input, correct_input):
    """Returns True if the user_input is inside correct_input (list) False in other way."""
    if user_input in correct_input:
        return True
    else:
        return False
