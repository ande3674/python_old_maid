import card
import random

class Deck():

    deck = []

    def __init__(self):
        # Add cards to the deck from file
        fin = open('deck_items.txt', 'rt')
        while True:
            line = fin.readline()
            if not line:
                break
            self.deck.append(line.strip())
        fin.close()


        # shuffle the deck
        #random.shuffle(self.deck)

        # for the game of old maid, we must remove one card,
        # which becomes the "old maid" card
        # self.deck.pop(0)


    def displayDeck(self):
        for c in self.deck:
            print(c)

    def displayHand(self, hand):
        for c in hand:
            c.displayCard()

    def dealCard(self):
        if len(self.deck) > 0:
            return self.deck.pop(0)
        else:
            return None

    def dealOldMaidHands(self):
        # We need two old maid hands.
        # Our deck is already shuffled, so we will just give the first half to the computer
        # and we will give the second half to the player :-)
        computerHand = self.deck[:26]
        playerHand = self.deck[26:]
        return computerHand, playerHand









