import card
import random

class Deck():

    def __init__(self):

        self.deck = []
        # Add 52 cards to the deck
        for s in ('hearts', 'spades', 'diamonds', 'clubs'):

            for v in ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'):
                c = card.Card(s, v)
                self.deck.append(c)
        random.shuffle(self.deck)


    def displayDeck(self):
        for c in self.deck:
            c.displayCard()

    def shuffleDeck(self):
        random.shuffle(self.deck)






