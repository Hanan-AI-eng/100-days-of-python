import random
print(r"""
 ▄████  █    ██ ▓█████   ██████   ██████  ██▓ ███▄    █   ▄████      ▄████  ▄▄▄       ███▄ ▄███▓▓█████ 
 ██▒ ▀█▒ ██  ▓██▒▓█   ▀ ▒██    ▒ ▒██    ▒ ▓██▒ ██ ▀█   █  ██▒ ▀█▒    ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ 
▒██░▄▄▄░▓██  ▒██░▒███   ░ ▓██▄   ░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒██░▄▄▄░   ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███   
░▓█  ██▓▓▓█  ░██░▒▓█  ▄   ▒   ██▒  ▒   ██▒░██░▓██▒  ▐▌██▒░▓█  ██▓   ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ 
░▒▓███▀▒▒▒█████▓ ░▒████▒▒██████▒▒▒██████▒▒░██░▒██░   ▓██░░▒▓███▀▒   ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒
 ░▒   ▒ ░▒▓▒ ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒  ░▒   ▒     ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░
  ░   ░ ░░▒░ ░ ░  ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░  ░   ░      ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░
░ ░   ░  ░░░ ░ ░    ░   ░  ░  ░  ░  ░  ░   ▒ ░   ░   ░ ░ ░ ░   ░    ░ ░   ░   ░   ▒   ░      ░      ░   
      ░    ░        ░  ░      ░        ░   ░           ░       ░          ░       ░  ░       ░      ░  ░
                                                                                                        """)
print("Welcome to the Number Guessing Game!")
print("I'm Thinking if a number between 1 and 100.")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
number=random.choice(num)

easy_attempt=10
hard_attempt=5

def easy():
    global easy_attempt
    while easy_attempt!=0:
        print(f"You have {easy_attempt} remaining to guess the number.")
        guess=int(input("Make a guess:"))
        if guess<number:
            print("Too low!")
            print("Guess Again")
            easy_attempt-=1
        elif guess>number:
            print("Too high!")
            print("Guess Again")
            easy_attempt -= 1
        elif guess==number:
            print(f"You got it! The answer was {number}")
            return
    print("You've run out of guesses. Refresh the page to run again.")

def hard():
    global hard_attempt
    while hard_attempt != 0:
        print(f"You have {hard_attempt} remaining to guess the number.")
        guess = int(input("Make a guess:"))
        if guess < number:
            print("Too Low!")
            print("Guess Again")
            hard_attempt -= 1
        elif guess > number:
            print("Too high!")
            print("Guess Again")
            hard_attempt -= 1
        elif guess == number:
            print(f"You got it! The answer was {number}")
    print("You've run out of guesses. Refresh the page to run again.")
 
if difficulty == "easy":
    easy()

elif difficulty == "hard":
    hard()
