import card
import deck
import oldmaid_deck

def gamePlay():

    ### Play Old Maid...
    print("Are you ready to play? Dealing hands...")
    computerHand, playerHand = oldmaid_deck.OldMaidDeck().deallHands()

    #print(computerHand)
    #print()
    #print(playerHand)

    ### Display the player's hand
    print("Here is your hand: ")
    print(playerHand)

    ### Remove the matches
    print("I will remove all of your matches now...")
    playerHand = removeMatches(playerHand)
    computerHand = removeMatches(computerHand)

    ### Display new hand
    print("Here is your hand without matches... ")
    print(playerHand)

def removeMatches(hand):

    for card in hand:
        if hand.count(card) == 2:
            hand.remove(card)
            hand.remove(card)
    return hand


def test():

    deck = oldmaid_deck.OldMaidDeck()
    deck.displayDeck()

    c, p = deck.deallHands()
    print("Computer hand is...", len(c), "elements long")
    print(c)
    print()

    print("Player hand is...", len(p), "elements long")
    print(p)

#test()
gamePlay()