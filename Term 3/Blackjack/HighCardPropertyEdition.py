# Karter Ence
# High Card (Property Edition)
# 2/13/2020
from Card import *

class HighCard(PositionableCard):
    def __init__(self, rank, suit):
        super(HighCard, self).__init__(rank, suit, faceUp=True)

    @property
    def value(self):
        if self.isFaceUp:
            v = HighCard.RANKS.index(self.rank) + 1
            if v == 1:
                v += 13
        else:
            v = None
        return v

    def __str__(self):
        rep = str.format("""
         _________
        |{0:2}       |
        |{1:2}       |
        |         |
        |       {0:2}|
        |       {1:2}|
        |_________|
        value = 
        """, self.rank, self.suit)
        return rep

class HighCardDeck(Deck):
    def populate(self):
        for suit in HighCard.SUITS:
            for rank in HighCard.RANKS:
                self.add(HighCard(rank, suit))

class HighCardHand(Hand):
    def __init__(self, name):
        super(HighCardHand, self).__init__()
        self.name = name
    
    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        for card in self.cards:
            t += card.value
        return t

    def win(self):
        print(self.name)
        print("Winner")
    def lose(self):
        print(self.name)
        print("Looser! Noob.")

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
            values.append(value)
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
        hand = HighCardHand(x)
        hands.append(hand)
    deck = HighCardDeck()
    deck.populate()
    deck.shuffle()
    deck.deal(hands, 1)
    highCard = 0
    for player in hands:
        print(player)
        if player.total > highCard:
            highCard = player.total
    for player in hands:
        if player.total >= highCard:
            player.win()
        else:
            player.lose()

main()
