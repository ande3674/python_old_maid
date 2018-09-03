import oldmaid_deck
import computer_hand
import player_hand
import random

def gamePlay():

    ### Play Old Maid...
    print("Are you ready to play OLD MAID? Dealing hands...")
    print()
    computerHand, playerHand = oldmaid_deck.OldMaidDeck().deallHands()

    #print(computerHand)
    #print()
    #print(playerHand)

    ### Display the player's hand
    print("Here is your initial deal: ")
    print(playerHand)
    print()

    ### Remove the matches
    input("I will remove all of your matches now... (PRESS ENTER)")
    print()
    # Now use our HAND CLASSES TO MANAGE THE HANDS
    playerHandClassVersion = player_hand.PlayerHand(playerHand)
    computerHandClassVersion = computer_hand.ComputerHand(computerHand)

    ### Display new hand
    print("Here is your hand without matches... ")
    playerHandClassVersion.displayHand()
    print()

    ### Now we play...
    # while there are more cards left to pick other than the old maid...

    # TODO
    # the while loop should only do one turn per loop
    # must keep track of whose turn it is

    while playerHandClassVersion.getPlayerHandSize() + computerHandClassVersion.getComputerHandSize() > 1:
        ### Pick a card from the computer's hand
        size = computerHandClassVersion.getComputerHandSize()
        print("Pick a card from the computer, enter a card number between 1 and", size)
        index = input(" ")
        while not (1 <= int(index) <= size):
            index = input("Invalid number, try again.")

        ### Check for / discard any new matches
        tempCard = computerHandClassVersion.removeCard(int(index) - 1)
        print("You picked this card: '", tempCard, "' and we will now check for & remove any matches... (PRESS ENTER)")
        #playerHand.append(tempCard)
        #playerHand = removeMatches(playerHand)
        playerHandClassVersion.addCardRemoveMatches(tempCard)
        print()

        print("Here is your updated hand: ")
        playerHandClassVersion.displayHand()
        print()

        input("Press Enter to allow computer to take its turn...(PRESS ENTER)")

        ### Computer picks a card from player hand
        pHandSize = playerHandClassVersion.getPlayerHandSize()
        randomIndex = random.randint(0, pHandSize-1)
        tempCardForComputer = playerHandClassVersion.removeCard(randomIndex)

        print("The computer picked '", tempCardForComputer, "'")
        print()

        print("Here is your updated hand: ")
        playerHandClassVersion.displayHand()

        ### Check for / discard any new matches
        computerHandClassVersion.addCardRemoveMatches(tempCardForComputer)


        ### Play until 1 card left, declare winner.


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