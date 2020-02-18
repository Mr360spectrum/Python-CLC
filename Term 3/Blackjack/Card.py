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
            # rep = "Your hand:\n"
            for card in self.cards:
                rep = str(card) + " "
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

class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, hands, perHand=1):
        for rounds in range(perHand):
            for hand in hands:
                if self.cards:
                    topCard = self.cards[0]
                    self.give(hand, topCard)
                else:
                    print("Out of cards.")

class PositionableCard(Card):
    def __init__(self, rank, suit, faceUp = False):
        super(PositionableCard, self).__init__(rank, suit)
        self.isFaceUp = faceUp

    def __str__(self):
        if self.isFaceUp:
            rep = super(PositionableCard, self). __str__()
        else:
            rep = """
         _________
        |c        |
        |a       d|
        |r   no  r|
        |d       a|
        |        c|
        |_________|
        """
        return rep

    def flip(self):
        self.isFaceUp = not self.isFaceUp

class PositionableDeck(Deck):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(PositionableCard(rank, suit))
