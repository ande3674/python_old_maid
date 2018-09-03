import random

class ComputerHand():

    def __init__(self, card_list):
        for card in card_list:
            if card_list.count(card) == 2:
                card_list.remove(card)
                card_list.remove(card)
        self.hand = card_list


    def removeCard(self, index):
        return self.hand.pop(index)

    def addCardRemoveMatches(self, card):
        # if the card is already in the hand, then it'll be a match and they will both have to be removed
        if card in self.hand:
            self.hand.remove(card)
        #else we add the card to the hand
        else:
            self.hand.append(card)
        # finally, shuffle again
        random.shuffle(self.hand)

    def getComputerHandSize(self):
        return len(self.hand)

    def displayHand(self):
        print(self.hand)