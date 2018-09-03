import random

class OldMaidDeck():

    def __init__(self):
        # Add our made up cards to the deck
        self.deck = ['bunny', 'bunny', 'dog', 'dog', 'kitty', 'kitty', 'bear', 'bear', 'mouse', 'mouse', 'duck', 'duck',
                     'horse', 'horse', 'frog', 'frog', 'bird', 'bird', 'skunk', 'skunk', 'cow', 'cow', 'pig', 'pig', 'old maid']

        # shuffle the deck
        random.shuffle(self.deck)

    def displayDeck(self):
        for c in self.deck:
            print(c)

    def deallHands(self):
        half = ( len(self.deck) // 2 ) + 1
        computerHand = self.deck[:half]
        playerHand = self.deck[half:]
        return computerHand, playerHand