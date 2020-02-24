# Karter Ence
# Card (Blackjack)
# 2/11/2020
import random

class Card(object):
    """The cards themselves. They have ranks, suits, and can be flipped."""
    RANKS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    SUITS = ("♤", "♥", "♢", "♣")
    
    def __init__(self, rank, suit, faceUp=True):
        self.rank = rank
        self.suit = suit
        self.isFaceUp = faceUp

    def flip(self):
        # Invert isFaceUp
        self.isFaceUp = not self.isFaceUp

    def __str__(self):
        if self.isFaceUp:
            rep = str.format("""
         _________
        |{0:2}       |
        |{1:2}       |
        |         |
        |       {0:2}|
        |       {1:2}|
        |_________|
        """, self.rank, self.suit)
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

class Hand(object):
    """The thing that holds cards."""
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            # rep = "Your hand:\n"
            for card in self.cards:
                # Display each card
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
    """A deck of playing cards. Can be populated with cards, shuffled, and can deal out cards."""
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

if __name__ == "__main__":
    print("This is a module with classes for playing cards.")
    print("It is not meant to be run by itself.")
    print("Press the enter key to exit.")
    input()
