# Karter Ence
# High Card
# 2/13/2020
from Card import *

class HighCard(Card):
    def __init__(self, rank, suit, value):
        super(HighCard, self).__init__(rank, suit)
        self.value = value

    def __str__(self):
        rep = str.format("""
         _________
        |{0:2}       |
        |{1:2}       |
        |         |
        |       {0:2}|
        |       {1:2}|
        |_________|
        value = {2}
        """, self.rank, self.suit, self.value)
        return rep

class HighCardDeck(Deck):
    def populate(self):
        for suit in HighCard.SUITS:
            for rank in HighCard.RANKS:
                if rank == "A":
                    value = 14
                elif rank == "J":
                    value = 11
                elif rank == "Q":
                    value = 12
                elif rank == "K":
                    value = 13
                else:
                    value = rank
                self.add(HighCard(rank, suit, value))

def getName():
    name = ""
    while name == "":
        print("Enter your name.")
        name = input(": ")
    return name

def findWinner(hands, names):
    values = []
    winMessage = ""
    for hand in hands:
        for card in hand.cards:
            value = card.value
            values.append(int(value))
    highest = max(values)
    if values.count(int(highest)) > 1:
        winMessage = "It's a tie!"
        return winMessage
    highestIndex = values.index(highest)
    winner = names[highestIndex]
    winMessage = "The winner is: " + winner
    return winMessage

def main():
    print("How many players are there?")
    totalPlayers = int(input(": "))
    names = []
    hands = []
    for i in range(totalPlayers):
        x = getName()
        hand = Hand()
        hands.append(hand)
        names.append(x)
    deck = HighCardDeck()
    deck.populate()
    deck.shuffle()
    deck.deal(hands, 1)
    for hand in hands:
        nameIndex = hands.index(hand)
        handName = names[nameIndex]
        print(handName + "'s hand:", hand)
    winMessage = findWinner(hands, names)
    print(winMessage)

main()
