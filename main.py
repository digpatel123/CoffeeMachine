from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

main_coffee_maker = CoffeeMaker()
coin_machine = MoneyMachine()

machine_is_on = True

while machine_is_on:
    menu = Menu()
    menu_item_names = menu.get_items().split("/")
    prompt_for_drink = (input(f"What drink would you like to have: {menu_item_names[0]}, {menu_item_names[1]}, {menu_item_names[2]}?")).lower()

    if prompt_for_drink == "report":
        main_coffee_maker.report()
        coin_machine.report()
    elif prompt_for_drink == "off":
        machine_is_on = False
    else:
        drink = menu.find_drink(prompt_for_drink)
        if main_coffee_maker.is_resource_sufficient(drink):
            if coin_machine.make_payment(drink.cost):
                main_coffee_maker.make_coffee(drink)




