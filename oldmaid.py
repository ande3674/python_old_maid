import oldmaid_deck
import computer_hand
import player_hand

def gamePlay():

    ### Play Old Maid...
    print("Are you ready to play? Dealing hands...")
    computerHand, playerHand = oldmaid_deck.OldMaidDeck().deallHands()

    #print(computerHand)
    #print()
    #print(playerHand)

    ### Display the player's hand
    print("Here is your initial deal: ")
    print(playerHand)

    ### Remove the matches
    input("I will remove all of your matches now... (PRESS ENTER)")
    # Now use our HAND CLASSES TO MANAGE THE HANDS
    playerHandClassVersion = player_hand.PlayerHand(playerHand)
    computerHandClassVersion = computer_hand.ComputerHand(computerHand)

    ### Display new hand
    print("Here is your hand without matches... ")
    playerHandClassVersion.displayHand()

    ### Now we play...
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

    print("Here is your updated hand: ")
    playerHandClassVersion.displayHand()
    input("Press Enter to allow computer to take its turn...(PRESS ENTER)")


    ### Computer picks a card from player hand
    ### Check for / discard any new matches
    ### Shuffle hand
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