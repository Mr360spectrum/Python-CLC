import Cards as C
import Games as G

class WarCard(C.Card):
    """A War Card"""

    @property
    def value(self):
        if WarCard.RANKS.index(self.rank) + 1 == 1:
            v = 14
        else:
            v = WarCard.RANKS.index(self.rank) + 1
        return v


class WarHand(C.Hand):
    """A War Hand"""

    def __init__(self, name):
        super(WarHand, self).__init__()
        self.name = name

    def __str__(self):
        rep = f"{self.name} :\t" + super(WarHand, self).__str__()
        return rep


class WarDeck(C.Deck):
    """A War Deck"""
    def populate(self):
        for suit in WarCard.SUITS:
            for rank in WarCard.RANKS:
                self.add(WarCard(rank, suit))


class WarPot(C.Hand):
    """The Pot which takes from the Table and gives to the Overall Winner."""
    def giveCards(self, winner):
        for c in self.cards:
            self.give(winner, c)


class WarTable(C.Hand):

    def give(self, otherHand, cards, winner):
        for card in cards:
            otherHand.add(otherHand, card)
            self.cards.remove(card)
        WarPot.giveCards(winner)

    def findWinner(self, players):
        goToWar = False
        if self.cards[0].value > self.cards[1].value:
            print("Player 1 wins.")
            self.give(WarPot, self.cards, players[0])
        elif self.cards[0].value < self.cards[1].value:
            print("Player 2 wins.")
            self.give(WarPot, self.cards, players[1])
        else:
            print("Time for War")
            goToWar = True
        return goToWar


class WarPlayer(WarHand):

    def playCard(self, otherHand):
        print(self.cards)
        self.give(otherHand, self.cards[0])
        print(self.cards[0])
        self.cards.remove(self.cards[0])

    def win(self):
        print(f"{self.name} has crushed the competition!")

    def lose(self):
        print(f"{self.name} has been annihilated.")


class WarGame(object):
    """A Game of War"""

    def __init__(self, names):
        self.players = []
        for name in names:
            player = WarPlayer(name)
            self.players.append(player)
        self.deck = WarDeck()
        self.deck.populate()
        self.deck.shuffle()
        self.table = WarTable()
        self.pot = WarPot()

    def war(self):
        for player in self.players:
            for i in range(3):
                player.give(self.pot, player.cards[0])
            player.give(self.table, player.cards[0])

    def play(self):
        self.deck.deal(self.players, perHand=26)
        for player in self.players:
            player.playCard(self.table)
        goToWar = self.table.findWinner(self.players)
        while goToWar:
            self.war()
            goToWar = self.table.findWinner(self.players)
        if not player[0].cards:
            player[0].lose()
            player[1].win()
        elif not player[1].cards:
            player[1].lose()
            player[0].win()


def main():
    print("\t\tWelcome to War!\n")
    names = []
    for i in range(2):
        name = input(f"Enter player {i + 1}'s name: ")
        names.append(name)
    game = WarGame(names)

    again = None

    while again != "n":
        game.play()
        again = G.yes_no("\nDo you want to play again? (Y/N)")

main()











