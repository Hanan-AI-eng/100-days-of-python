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


Water=300
Milk=200
Coffee=100
money=0

def report():

    print("Water:",Water)
    print("Milk:",Milk)
    print("Coffee:",Coffee)
    print("Money:",money)
    return


def info_drink_espresso():
    water=MENU["espresso"]["ingredients"]["water"]
    coffee=MENU["espresso"]["ingredients"]["coffee"]
    if water>Water:
        print("Sorry there is not enough water")
    if coffee>Coffee:
        print("Sorry there is not enough coffee")

def info_drink_latte():
    water=MENU["latte"]["ingredients"]["water"]
    milk=MENU["latte"]["ingredients"]["water"]
    coffee=MENU["latte"]["ingredients"]["coffee"]
    if water>Water:
        print("Sorry there is not enough water")
        return
    if coffee>Coffee:
        print("Sorry there is not enough coffee")
        return
    if milk>Milk:
        print("Sorry there is not enough milk")
        return

def info_drink_cappuccino():
    water = MENU["cappuccino"]["ingredients"]["water"]
    milk = MENU["cappuccino"]["ingredients"]["water"]
    coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    if water > Water:
        print("Sorry there is not enough water")
        return
    if coffee > Coffee:
        print("Sorry there is not enough coffee")
        return
    if milk > Milk:
        print("Sorry there is not enough milk")
        return




def coffeee():

    global Water
    global Milk
    global Coffee
    global money
    m=0
    next_customer=True
    Iwant=False
    while next_customer:
        start=input("What would you like? (espresso/latte/cappuccino): ").lower()
        if start == "off":  # put it at the end later
            return
        if start == "report":
            report()
            coffeee()


        print("Please insert coins")
        quarters_user=int(input("How many quarters? "))
        dimes_user=int(input("How many dimes? "))
        nickles_user=int(input("How many nickles? "))
        pennies_user=int(input("How many pennies? "))
        quarters = 0.25
        dimes = 0.10
        nickles = 0.05
        pennies = 0.01
        total=(quarters_user*quarters) + (dimes_user * dimes) + (nickles_user * nickles) + (pennies_user * pennies)
        m += total
        money=round(m,2)


        if start == "latte":

            info_drink_latte()


            if money < MENU["latte"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            elif money >= MENU["latte"]["cost"]:
                Water -= MENU["latte"]["ingredients"]["water"]
                Milk -= MENU["latte"]["ingredients"]["milk"]
                Coffee -= MENU["latte"]["ingredients"]["coffee"]
                Iwant=True
            if money>MENU["latte"]["cost"]:
                money-=MENU["latte"]["cost"]
                Iwant = True




        if start=="cappuccino":

            info_drink_cappuccino()
            if money < MENU["cappuccino"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            elif money >= MENU["cappuccino"]["cost"]:
                Water -= MENU["cappuccino"]["ingredients"]["water"]
                Milk -= MENU["cappuccino"]["ingredients"]["milk"]
                Coffee -= MENU["cappuccino"]["ingredients"]["coffee"]
                Iwant = True
            if money > MENU["cappuccino"]["cost"]:
                money -= MENU["cappuccino"]["cost"]
                Iwant = True



        if start=="espresso":

            info_drink_espresso()
            if money < MENU["espresso"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            elif money >= MENU["espresso"]["cost"]:
                Water -= MENU["espresso"]["ingredients"]["water"]
                Coffee -= MENU["espresso"]["ingredients"]["coffee"]
                Iwant = True
            if money > MENU["espresso"]["cost"]:
                money -= MENU["espresso"]["cost"]
                Iwant = True
        if Iwant:

            print(f"Here is {money} dollars in change")
            print("Here is your latte. Enjoy!")


coffeee()

