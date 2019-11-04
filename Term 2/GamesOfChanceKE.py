# Karter Ence
# Games of Chance
# 11/4/2019
import random

deck = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
# shuffle the deck
random.shuffle(deck)
# print the results
print(deck)
# get random card index from 0 through 12
cardIndex = random.randint(0, 12)
# get and print card at that position
card = deck[cardIndex]
print(str.format("Card at index {} = '{}'", cardIndex, card))

coinFlipOptions = ("Heads","Tails")
for i in range(0,5):
    flip = random.choice(coinFlipOptions)
    print("Coin-flip results:", flip)
# get random choice from coinFlipOptions and print results