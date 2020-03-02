import Cards as C
import Games as G


class WarCard(C.Card):
    """A War Card"""

    @property
    def value(self):
        # Find the value of the card using its rank
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
    def war(self, players):
        # If any of the players has less than 4 cards at the beginning of war,
        # clear their hand. This will determine who wins and who loses later on.
        if len(players[0].cards) < 4:
            players[0].clear()
        elif len(players[1].cards) < 4:
            players[1].clear()
        else:
            print("Time for War")
            # Each player gives 3 cards to the war pot
            for player in players:
                    for i in range(3):
                        player.give(self, player.cards[0])

    def giveCards(self, players, winner):
        if winner != "Tie":
            # Give the winner all of the cards
            for i in range(len(self.cards)):
                self.give(players[winner], self.cards[0])
        else:
            self.war(players)


class WarTable(C.Hand):

    def findWinner(self, WarPot, players):
        # If a player has no cards, the other one wins.
        if self.cards[0].value > self.cards[1].value:
            print(f"{players[0].name} wins.")
            winner = 0
        elif self.cards[0].value < self.cards[1].value:
            print(f"{players[1].name} wins.")
            winner = 1
        else:
            winner = "Tie"
        for i in range(len(self.cards)):
            self.give(WarPot, self.cards[0])
        return winner


class WarPlayer(WarHand):

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

    def play(self):
        playing = True
        self.deck.deal(self.players, perHand=26)
        while playing:
            for player in self.players:
                # Print both cards, then each player plays that card
                print(player.cards[0])
                player.give(self.table, player.cards[0])
            input("Press Enter to continue")
            # Find the winner
            winner = self.table.findWinner(self.pot, self.players)
            # The pot give the winner all cards
            self.pot.giveCards(self.players, winner)
            if not self.players[0].cards:
                playing = False
                self.players[0].lose()
                self.players[1].win()
            if not self.players[1].cards:
                playing = False
                self.players[1].lose()
                self.players[0].win()

def main():
    print("\t\tWelcome to War!\n")
    names = []
    for i in range(2):
        name = input(f"Enter player {i + 1}'s name: ")
        names.append(name)

    again = None

    while again != "n":
        game = WarGame(names)
        game.play()
        again = G.askYesNo("\nDo you want to play again? (Y/N)")

main()
