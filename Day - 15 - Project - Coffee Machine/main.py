import os
import time
import art

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

profit = 0
resources = {
    "water": 800,
    "milk": 500,
    "coffee": 300,
}


# TODO 1 : Check whether resource is sufficient to make the ordered drink?
def is_resource_sufficient(order_ingredients):
    """ Returns True when order can be made. False when ingredients are insufficient. """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"\n Sorry there is not enough {item}. ")
            return False
    return True


# TODO 2 : Process coins means calculate the the total value of the inserted coins by the user
def process_coin():
    """ Returns the total calculated from coins inserted. """
    print("\n Please insert coins. ")
    total_money = int(input(" How many quarters? : ")) * 0.25
    total_money += int(input(" How many dimes? : ")) * 0.1
    total_money += int(input(" How many nickels? : ")) * 0.05
    total_money += int(input(" How many pennies? : ")) * 0.01

    return total_money


# TODO 3 : Check whether the transaction made by the user is successful or not
def transaction_successful(money_received, drink_cost):
    """ Return True when the payment is accepted. Or False if money is insufficient. """
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"\n Here is ${change} dollars in change. ")
        global profit
        profit += drink_cost
        return True
    elif money_received == drink_cost:
        return True
    else:
        print("\n Sorry that's not enough money. Money refunded. ")
        return False


# TODO 4 : Make coffee by the entered choice of user
def make_coffee(drink_name, order_ingredients):
    """ Deduct the required ingredients from the resources. """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"\n Here is your {drink_name} ☕. ENJOY YOUR DRINK !! ")


# TODO 5 : Call all the above declared functions and execute it.
# Initially setting that Coffee Machine is ON
is_coffee_machine_on = True
while is_coffee_machine_on:

    print(art.on_logo)

    # Asking the user to enter their choice of Coffee
    user_choice = input("\n What would you like? (espresso/latte/cappuccino): ").lower()

    # Checking if the secret word OFF is pressed or not and if it's pressed then TURN OFF the machine for maintenance
    if user_choice == "off":
        os.system('cls')
        print(art.off_logo)
        time.sleep(5)
        print("\n\t\t\t\tCOFFEE MACHINE TURNED OFF. ")
        is_coffee_machine_on = False

    # Checking if the user pressed REPORT to check the status of the ingredients available in the Coffee Machine
    elif user_choice == "report":
        print(f"\t\t\tWater : {resources['water']}ml")
        print(f"\t\t\tMilk : {resources['milk']}ml")
        print(f"\t\t\tCoffee : {resources['coffee']}g")
        print(f"\t\t\tMoney : ${profit}")

    # If the user pressed their choice of Coffee
    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if transaction_successful(money_received=payment, drink_cost=drink["cost"]):
                make_coffee(drink_name=user_choice, order_ingredients=drink["ingredients"])
