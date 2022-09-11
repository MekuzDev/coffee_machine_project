from app_data import MENU, resources


# TODO:: accept coins
def process_coin():
    tot = 0
    quarter = float(input("How many quarters ? "))
    penny = float(input("How many pennies ? "))
    nickel = float(input("How many nickles ? "))
    dime = float(input("How many dimes ? "))
    tot += 0.25 * quarter + 0.01 * penny + 0.05 * nickel + 0.10 * dime
    return tot


# TODO:: Get cost of coffee
def get_coffee_cost(coffee):
    return MENU[coffee]['cost']


program_ended = False
money = 0
while not program_ended:
    # TODO:: Machine says welcome and displays the menus item and prices
    print('Welcome To CC Jitters digital')
    # TODO:: Ask the customer what they'd like from the menu
    menu_item = input("What would you like today (Espresso, Latte, Cappuccino)").lower()
    resources['money'] = f"${money}"
    if menu_item == 'off':
        print("Bye!!, Come coffee another say")
        program_ended = True
    elif menu_item == 'report':
        for i in resources:
            print(f"{i}:{resources[i]}")
    elif menu_item == 'espresso' or 'latte' or 'cappuccino':
        recipe = MENU[menu_item]['ingredients']
        # TODO:: Check if resources is sufficient for coffee
        if recipe['water'] > resources['water']:
            print(f"Not enough water to make {menu_item}")
        elif recipe['milk'] > resources['milk']:
            print(f"Not enough milk to make {menu_item}")
        elif recipe['coffee'] > resources['milk']:
            print(f"Not enough coffee to make {menu_item}")
        else:
            total = process_coin()
            if total >= MENU[menu_item]['cost']:
                for i in recipe:
                    resources[i] = resources[i] - recipe[i]
                change = total - MENU[menu_item]['cost']
                money += MENU[menu_item]['cost']
                print(f'you have ${round(change,2)} in change')
                print(f"here's your {menu_item} ☕ ")
                print('_________________________________________')
            else:
                print('insufficient funds')
                for i in resources:
                    print(f"{i}:{resources[i]}")

                print('_________________________________________')
