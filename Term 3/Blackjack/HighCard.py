# Karter Ence
# High Card
# 2/13/2020
import Card

class HighCardDeck(Card.Deck):
    pass

def getName():
    name = ""
    while name == "":
        print("Enter your name.")
        name = input(": ")
    return name

print("How many players are there?")
totalPlayers = int(input(": "))
names = []
hands = []
for i in range(totalPlayers):
    x = getName()
    hand = Card.Hand()
    hands.append(hand)
    names.append(x)
deck = Card.Deck()
deck.populate()
deck.shuffle()
deck.deal(hands, 1)

for hand in hands:
    print(hand)