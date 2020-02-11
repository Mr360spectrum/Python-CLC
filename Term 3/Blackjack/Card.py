# Karter Ence
# Card (Blackjack)
# 2/11/2020
import random

class Card(object):
    RANKS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    SUITS = ("♤", "♥", "♢", "♣")
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = str.format("""
         _________
        |{0:2}       |
        |{1:2}       |
        |         |
        |       {0:2}|
        |       {1:2}|
        |_________|
        """, self.rank, self.suit)
        return rep

class Hand(object):
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = "Your hand:\n"
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "Empty hand."
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, otherHand, card):
        self.cards.remove(card)
        otherHand.add(card)

myHand = Hand()
yourHand = Hand()
for i in range(5):
    card = Card(random.choice(Card.RANKS), random.choice(Card.SUITS))
    print(card)
    myHand.add(card)

print(myHand)
print(yourHand)

myHand.give(yourHand, myHand.cards[0])
print(yourHand)
print(myHand)
myHand.clear()
yourHand.clear()
print(myHand, yourHand)