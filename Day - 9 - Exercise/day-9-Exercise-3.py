import os
import art

print(art.logo)
print(art.wishing_logo)
bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    winner = ""
    highest_bid = 0
    for bidder in bidding_record:
        bid_value = bidding_record[bidder]
        if bid_value > highest_bid:
            highest_bid = bid_value
            winner = bidder
    print(art.winner_logo)
    print(f"\n The winner is {winner} with a bid of ₹{highest_bid}")


while not bidding_finished:
    name = input("What is your name? : ")
    price = int(input("\nWhat's your bid? : ₹"))
    bids[name] = price
    should_continue = input("\nAre there any other bidders? Type 'Yes' or 'No'. -> ").lower()
    if should_continue == "no":
        bidding_finished = True
        os.system('cls')
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system('cls')
