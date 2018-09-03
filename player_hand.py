import random

class PlayerHand():

    def __init__(self, cardList):
        listOfCardsToRemove = []
        for card in cardList:
            if cardList.count(card) == 2:
                listOfCardsToRemove.append(card)
        for c in listOfCardsToRemove:
            cardList.remove(c)
        self.hand = cardList

    def removeCard(self, index):
        return self.hand.pop(index)

    def addCardRemoveMatches(self, card):
        # if the card is already in the hand, then it'll be a match and they will both have to be removed
        if card in self.hand:
            self.hand.remove(card)
        # else we add the card to the hand
        else:
            self.hand.append(card)
        # finally, shuffle again
        random.shuffle(self.hand)

    def getPlayerHandSize(self):
        return len(self.hand)

    def displayHand(self):
        print(self.hand)