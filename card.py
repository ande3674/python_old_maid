
class Card():

    def __init__(self, suit, value):
        self.__suit = suit
        self.__value = value

    @property
    def suit(self):
        return self.__suit

    @property
    def value(self):
        return self.__value

    def displayCard(self):
        print(self.__value, "of", self.__suit)