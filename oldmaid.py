import oldmaid_deck
import computer_hand
import player_hand
import random

### Old Maid game
# The deck can be anything as long as every "card" has a match and there is one
# single Old Maid card
# The deck can be set up in deck_items.txt
# List two of each "card" and one "OLD MAID"

def main():

    ### HERE IS THE GAME SETUP ###
    ### Play Old Maid...
    print("Are you ready to play OLD MAID? Dealing hands...")
    print()
    computerHand, playerHand = oldmaid_deck.OldMaidDeck().deallHands()

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

    ### NOW PLAY THE GAME ###
    gamePlay(playerHandClassVersion, computerHandClassVersion)


def gamePlay(pHand, cHand):

    # ### Play Old Maid... ### #
    # while there are more cards left to pick other than the old maid
    # the while loop should only do one turn per loop
    # must keep track of whose turn it is
    whoseTurn = 'p'

    while pHand.getPlayerHandSize() + cHand.getComputerHandSize() > 1:

        if whoseTurn == 'p':

            ### Pick a card from the computer's hand
            size = cHand.getComputerHandSize()
            print("Pick a card from the computer, enter a card number between 1 and", size)
            index = input(" ")
            while not (1 <= int(index) <= size):
                index = input("Invalid number, try again.")
            tempCard = cHand.removeCard(int(index) - 1)

            ### Check for / discard any new matches
            print("You picked this card: '", tempCard, "' and we will now check for & remove any matches... (PRESS ENTER)")
            pHand.addCardRemoveMatches(tempCard)
            print()

            ### Display current hand
            print("Here is your updated hand: ")
            pHand.displayHand()
            print()

            ### Change the turn variable and move on to next turn...
            whoseTurn = 'c'
            input("Press Enter to allow computer to take its turn...(PRESS ENTER)")
            print()

        else:

            ### Computer picks a card from player hand
            pHandSize = pHand.getPlayerHandSize()
            randomIndex = random.randint(0, pHandSize-1)
            tempCardForComputer = pHand.removeCard(randomIndex)
            print("The computer picked '", tempCardForComputer, "'")
            print()

            ### Display current hand
            print("Here is your updated hand: ")
            pHand.displayHand()
            print()

            ### Check for / discard any new matches from the computer's hand (behind the scenes)
            # Player does not need to know/see this
            cHand.addCardRemoveMatches(tempCardForComputer)

            ### Update whoseTurn variable and move onto next turn...
            whoseTurn = 'p'

    ### While loop ended which means the game is over and we have a winner
    declareWinner(pHand, cHand)


def declareWinner(playerHand, compHand):
    ### Play until 1 card left, declare winner.
    print("Here are the final hands: ")
    print("YOUR HAND: ")
    playerHand.displayHand()
    print()

    print("COMPUTER HAND: ")
    compHand.displayHand()
    print()

    if (compHand.getComputerHandSize() > 0):
        print("Congrats! YOU WIN!!!")
    else:
        print("Sorry! COMPUTER WINS!!!")

main()
