import random
import art
print(art.logo)
def deal_card():
    """ Return a random card from the deck """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return a score calculate from the card"""
    if 11 in cards and 10 in cards and len(cards)==2:
        return 0

    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
def compare(u_score, c_score):
    if u_score==c_score:
        return "Draw"
    elif c_score==0:
        return "Lose"
    elif u_score==0:
        return "Win"
    elif u_score>21:
        return "user lose"
    elif c_score>21:
        return "computer win"
    elif u_score>c_score:
        return "You win"
    else:
        return "you lose"


def playgame():
    print(art.logo)
    user_card=[]
    computer_card=[]
    computer_score=-1
    user_score=-1
    is_game_over=False


    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not is_game_over:
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)
        print(f"Your cards:{user_card} and {user_score}")
        print(f"computer first card:{computer_card[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            want=input("Type 'y' to get another card or type 'n' to end")
            if want=='y':
                user_card.append(deal_card())
            else:
                is_game_over=True
    while computer_score!=0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)

    print(compare(user_score, computer_score))

while input("Do you want to play another game? Type 'y' or 'n': "):
    print("\n"* 100)
    playgame()


# still_play=True
# target=0
#
# Ace=cards[0]
#
# start=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
# card_user=[]
# if start=='y':
#     user_card_1=random.choice(cards)
#     user_card_2=random.choice(cards)
#     user_total=user_card_1+user_card_2
#
#     computer_card_1=random.choice(cards)
#     computer_card_2=random.choice(cards)
#     computer_total=computer_card_1+computer_card_2
#
#     if (user_card_1==1 or 10) and (user_card_2==1 or 10):
#         print("You win!")
#     if (computer_card_1==1 or 10) and (computer_card_2==1 or 10):
#         print("You lose!")
#     if user_total>21:
#         if user_card_1==Ace or user_card_2==Ace:
#             Ace=1
#             user_total = user_card_1 + user_card_2
#
#             if user_total>21:
#                 print("You lose!")
#         else:
#             another_card=input("do you want another card? Type 'y' or 'n': ").lower()
#             if another_card=='y':
#                 addition_card=
#             elif another_card=='n':
#
#     else:
#         print("You lose!")
# else:
#     print("Goodbye")
