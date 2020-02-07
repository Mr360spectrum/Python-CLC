
from Cards import *

class Hand(object):
    def __init__(self):
        self.held = []
        
    def draw(self):
    while True:
        c = random.choice(Cards.CARDS)
        if (c not in cards.cardsDrawn) and (c not in cards.cardsDiscarded):
            cardsDrawn.append(c)
            return c

    def discard(self):
        cardToDiscard = self.held.pop[-1]
        Cards.cardsDiscarded.append(cardsToDi0.scard)
    