import machine_data

# TODO: ask user about the order - espresso/latte/cappuccino
coffee_type = input("What would you like? (espresso/latte/cappuccino)")
coffee_data = machine_data.MENU[coffee_type]

# TODO: verify if there are enough resources
# TODO: ask for coins - quarters 0.25, dimes 0.10, nickles 0.05, pennies 0.01
print("Please insert coins.")
quarters = input("How many quarters? ")
dimes = input("How many dimes? ")
nickles = input("How many nickles? ")
pennies = input("How many pennies? ")

# TODO: verify if there is enough money

# TODO: prepare coffee
print(f"Here is your {coffee_type}. Enjoy your beverage.")

# TODO: update report

# TODO: if input is "report" print amount of water, milk, coffee, money
# TODO: if input is "off" finish game
# TODO: if input not correct finish game/ ask again
