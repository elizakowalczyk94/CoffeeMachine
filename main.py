import machine_data

# TODO: ask user about the order - espresso/latte/cappuccino
coffee_type = input("What would you like? (espresso/latte/cappuccino)")
coffee_data = machine_data.MENU[coffee_type]

# TODO: verify if there are enough resources
# TODO: ask for coins - quarters 0.25, dimes 0.10, nickles 0.05, pennies 0.01
print("Please insert coins.")
user_quarters = int(input("How many quarters? "))
user_dimes = int(input("How many dimes? "))
user_nickles = int(input("How many nickles? "))
user_pennies = int(input("How many pennies? "))
machine_money = 0

# TODO: verify if there is enough money
def calculate_coins(quarters, dimes, nickles, pennies):
    """Returns the amount of money in $ that user inserted. Input is the number of coins user inserted."""
    total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    return total

# TODO: prepare coffee
print(f"Here is your {coffee_type}. Enjoy your beverage.")

# TODO: update report

# TODO: if input is "report" print amount of water, milk, coffee, money
# TODO: if input is "off" finish game
# TODO: if input not correct finish game/ ask again
