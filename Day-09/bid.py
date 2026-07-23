# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)


def the_big_bidder(bidding_dictionary):
    winner=""
    high_bid=0
    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if bid_amount > high_bid:
            high_bid=bid_amount
            winner=bidder
        print(f"the winner {winner} with a bid of ${high_bid}")
bid_dic={}
contiune=True
while contiune:
    name=input("What is your name?: ")
    bid=int(input("What is your bid?: $"))
    bid_dic.update({name:bid})
    another = input("is there any user who want to bid? type 'yes' or 'no':\n ").lower()
    if another=="no":
        contiune=False
        the_big_bidder(bid_dic)
    elif another=="yes":
        print("\n"*100)
    else:
        print("wrong input")
