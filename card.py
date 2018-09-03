
class Card():

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def getSuit(self):
        return self.suit
    def getValue(self):
        return self.value
    def displayCard(self):
        print(self.value, "of", self.suit)