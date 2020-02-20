# Karter Ence
# Blackjack Game
# 2/20/2020
import CardKE as C
import GameKE as G

class BJCard(C.Card):
    """A Blackjack card."""
    ACE_VALUE = 1
    @property
    def value(self):
        if self.isFaceUp:
            value = BJCard.RANKS.index(self.rank) + 1
            if value > 10:
                value = 10
        else:
            value = None
        return value

class BJDeck(C.Deck):
    """A Blackjack deck."""
    def populate(self):
        for suit in BJCard.SUITS:
            for rank in BJCard.RANKS:
                self.cards.append(BJCard(rank, suit))

class BJHand(C.Hand):
    """A Blackjack hand."""
    def __init__(self, name):
        super(BJHand, self).__init__()
        self.name = name
    
    def __str__(self):
        rep = self.name + ":\t" + super(BJHand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        # If a card has no value (i.e. if a card is face down), then total is None
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        for card in self.cards:
            t += card.value
        # Determine if the hand contains an Ace
        containsAce = False
        for card in self.cards:
            if card.value == BJCard.ACE_VALUE:
                containsAce = True
        # If hand contains Ace and total is low enough, treat Ace as 11
        if containsAce and (t <= 11):
            # Add only 10 since we've already added 1 for the Ace
            t += 10
        return t

    @property
    def isBusted(self):
        return self.total > 21

class BJPlayer(BJHand):
    """A Blackjack player."""
    def isHitting(self):
        response = G.askYesNo("\n" + self.name + ", do you want to hit? [y/n]")
        return response == "y"

    def bust(self):
        print(self.name, "busts.")
        self.lose()
    
    def lose(self):
        print(self.name, "loses.")

    def win(self):
        print(self.name, "wins.")

    def push(self):
        print(self.name, "pushes.")

class BJDealer(BJHand):
    """A Blackjack dealer."""
    def isHitting(self):
        return self.total < 17
    def flipFirstCard(self):
        firstCard = self.cards[0]
        firstCard.flip()

class BJGame(object):
    """A Blackjack game."""
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJPlayer(name)
            self.players.append(player)
        self.dealer = BJDealer("Dealerman")
        self.deck = BJDeck()
        self.deck.populate()
        self.deck.shuffle()
    
    @property
    def stillPlaying(self):
        sp = []
        for player in self.players:
            if not player.isBusted():
                sp.append(player)
        return sp
    
    def __additional_cards(self, player):
        while not player.isBusted and player.isHitting():
            self.deck.deal([player])
            print(player)
            if player.isBusted:
                player.bust()

    def play(self):
        # Deal 2 cards to every player, including the dealer
        self.deck.deal(self.players + [self.dealer], perHand=2) # Square brackets makes self.dealer become a list element
        self.dealer.flipFirstCard()
        for player in self.players:
            print(player)
        print(self.dealer)
        # Deal additional 2 cards to everyone
        
        for player in self.players:
            self.__additional_cards(player)
        
        # Reveal dealer's first card
        self.dealer.flipFirstCard()
        
        if not self.stillPlaying:
            # Since all players have busted, show the dealer's hand
            print(self.dealer)
        else:
            # Deal additional cards to dealer
            print(self.dealer)
            self.__additional_cards(self.dealer)
        
            if self.dealer.isBusted:
                for player in self.stillPlaying:
                    player.win()
            else:
                for player in self.stillPlaying:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()
        # Remove everyone's cards
        for player in self.players:
            player.close()
        self.dealer.clear()

def main():
    print("\t\tWelcome to Blackjack!\n")
    names = []
    number = G.askNumber("How many players? (1 - 7) ", low=1, high=8)
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)
    
    game = BJGame(names)

    again = None
    while again != "n":
        game.play()
        again = G.askYesNo("\nDo you want to play again?")

main()
            