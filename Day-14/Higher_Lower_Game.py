
import random
from art import logo,vs
from game_data import data
print(logo)
count=0

def  compare(c):
    """give the comparision"""
    it_is_correct = True

    while it_is_correct:
        if c>0:
            print(f"You're right! Current score: {c}")

        compare_first=random.choice(data)
        name=compare_first['name']
        description=compare_first['description']
        country=compare_first['country']
        print(f"Compare A: {name}, {description}, {country}.")

        print(vs)

        compare_second=random.choice(data)
        name=compare_second['name']
        description=compare_second['description']
        country=compare_second['country']
        print(f"Compare B: {name}, {description}, {country}.")

        num_first=compare_first["follower_count"]
        num_second= compare_second["follower_count"]
        who = input("Who has more followers? Type 'A' or 'B': ").lower()

        if who == "a":
            if num_first > num_second:
                c += 1

            else:
                it_is_correct = False

        elif who == "b":
            if num_second > num_first:
                c += 1

            else:
                it_is_correct = False


    print(f"Sorry, that's wrong. Final score:{c}")
compare(count)
