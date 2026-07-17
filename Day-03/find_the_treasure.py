print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
way=input("Which way do you want to go write 'left' or 'right' \n")

if way.lower()=="right":
    print("Game over you got burred with lava wak wak!!! \n")
elif way.lower()=="left":
    action=input("What do you want to do there type 'swim' or 'wait' \n")
    if action.lower()=="swim":
        print("Game over you don't even know how to swim and it fill with shark you got ate!!! \n")
    elif action.lower()=="wait":
        door=input("Choose one door to run into there is a"
                   " serial killer behind you now type 'red' or 'blue' or 'yellow' !!!\n")
        if door.lower()=="red":
            print("Game over the killer friends found you \n")
        elif door.lower()=="blue":
            print("Game over there is a trap here for you \n")
        elif door.lower()=="yellow":
            print("You Win in the life or death game!!!\n")
        else:
            print("wrong choose\n")
    else:
        print("wrong choose\n")
else:
    print("wrong choose\n")
