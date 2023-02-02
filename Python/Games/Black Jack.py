# Importing the random library
import random

# Function to generate a card & it's value
def cardGenerator():
    suitCollection = ("Spades", "Clubs", "Diamonds", "Harts")
    suit = str(random.choice(suitCollection))
    cardValue = int(random.randint(1, 13))
    if cardValue == 1:
        card = (f"Ace {str(suit)}", int(cardValue))
    elif cardValue == 11:
        card = (f"Jack {str(suit)}", int(cardValue))
    elif cardValue == 12:
        card = (f"Queen {str(suit)}", int(cardValue))
    elif cardValue == 13:
        card = (f"King {str(suit)}", int(cardValue))
    else:
        card = (f"{str(cardValue)} {str(suit)}", int(cardValue))
    return card

# Function to check whether a card is an Ace card and use the needed value
def calculateCurrentScore(currentTotal: int, cardValue: int, aceCount: int):
    if cardValue == 1:
        newTotal = currentTotal + 11
        if newTotal > 21:
            newTotal = currentTotal + 1
        else:
            aceCount = int(aceCount + 1)
    else:
        newTotal = currentTotal + cardValue
    if newTotal > 21:
        if aceCount == 1:
            newTotal = newTotal - 10
            aceCount = int(0)
        elif aceCount == 2:
            newTotal = newTotal - 20
            aceCount = int(0)
        elif aceCount == 3:
            newTotal = newTotal - 30
            aceCount = int(0)
    newTotal = (int(newTotal), int(aceCount))
    return newTotal

# Function asking if the user wants to play again
def playAgain(validExit):
    validRetry = False
    while not validRetry:
        retry = str(input("Would you like to play again? (Y/N)\n\n: ").lower())
        if retry == "yes" or retry == "y":
            validRetry = True
            print("\nReloading...")
        elif retry == "no" or retry == "n":
            validRetry = True
            validExit = True
        else:
            print("\nPlease enter either Yes or No!\n")
    return validExit

# Function to ask the user what they want to do next
def hitOrStand(firstAction):
    validAction = False
    if firstAction == True:
        while not validAction:
            action = str(input("What would you like to do? (1/2/3)\n\n1 = Hit\n2 = Stand\n3 = Double Down\n\n: "))
            if action.isdigit():
                if action == "1":
                    nextAction = int(1)
                    validAction = True
                elif action == "2":
                    nextAction = int(2)
                    validAction = True
                elif action == "3":
                    nextAction = int(3)
                    validAction = True
                else:
                    print("\nPlease enter a number between 1 and 3!\n")
            else:
                print("\nPlease enter a number between 1 and 3!\n")
    else:
        while not validAction:
            action = input(str("What would you like to do? (1/2/3)\n\n1 = Hit\n2 = Hold\n\n: "))
            if action.isdigit():
                if action == "1":
                    nextAction = int(1)
                    validAction = True
                elif action == "2":
                    nextAction = int(2)
                    validAction = True
                else:
                    print("\nPlease enter a number between 1 and 3!\n")
            else:
                print("\nPlease enter a number between 1 and 3!\n")
    nextActions = (nextAction, False)
    return nextActions

# Declearing main validation variables (FLAGS)
validExit = False

# Declearing initail variables
roundNumber = int(0)

# Declearing the initial money amount       #? Initial Money Amount
playerMoney = int(1000)

# Loop for the main game
while not validExit:
    # Increasing the round number by 1 each time the game loops
    roundNumber = int(roundNumber + 1)

    # Declearing in game variables & FLAGS
    firstAction = True
    validBet = False
    dealerAceCounter = int(0)
    playerAceCounter = int(0)
    cardsUsed = int(0)
    playerTotal = int(0)
    dealerTotal = int(0)
    
    # Generating all the cards needed for the game
    card1 = cardGenerator() # Dealer card 1
    card2 = cardGenerator() # Dealer card 2 (Hidden)
    card3 = cardGenerator() #? Player card 1
    card4 = cardGenerator() #? Player card 2
    card5 = cardGenerator() #? Player card 3
    card6 = cardGenerator() #? Player card 4
    card7 = cardGenerator() #? player card 5
    card8 = cardGenerator() # Dealer card 3
    card9 = cardGenerator() # Dealer card 4
    card10 = cardGenerator() # Dealer card 5

    # Place a money bet on whether or not you will win          #? Money betting statement / query
    while not validBet:
        roundBet = str(input(f"\nHow much money would you like to bet? You have £{str(playerMoney)}!\n\n: "))
        if roundBet.isdigit():
            roundBet = int(roundBet)
            if roundBet >= 10 and roundBet <= playerMoney:
                validBet = True
            else:
                print(f"\nPlease enter a number between £10 and £{str(playerMoney)}!")
        else:
            print(f"\nPlease enter a number between £10 and £{str(playerMoney)}!")

    # Print the dealer's first 2 cards, keeping the value of the second card hidden
    print("\nROUND " + str(roundNumber) + "!\n")
    print("DEALER\n")
    print("Card 1 | " + str(card1[0]))
    print("Card 2 | ???\n")

    # Calculate the dealers current score
    print(f"Dealer's Current Total = {str(card1[1])} + ???!\n")

    # Print the players first 2 cards
    print("PLAYER\n")
    print("Card 1 | " + str(card3[0]))
    print("Card 2 | " + str(card4[0]) + "\n")

    # Calculate the players current score
    calculateTotal = calculateCurrentScore(playerTotal, card3[1], playerAceCounter)
    calculateTotal = calculateCurrentScore(calculateTotal[0], card4[1], calculateTotal[1])
    playerTotal = int(calculateTotal[0])
    playerAceCounter = int(calculateTotal[1])
    print("Player's Current Total = " + str(playerTotal) + "\n")

    # Track how many cards you've drawn
    cardsUsed = int(cardsUsed + 2)

    # Check if your total score is 21 or greater
    if playerTotal < 21:
        # Ask what the player would like to do next
        returnedActions = hitOrStand(firstAction)
        nextAction = returnedActions[0]
        firstAction = returnedActions[1]
    else:
        nextAction = 2

    # Continue the game based on the players input
    if nextAction == 1:
        # Print the players 3 cards
        print("\nPLAYER\n")
        print("Card 1 | " + str(card3[0]))
        print("Card 2 | " + str(card4[0]))
        print("Card 3 | " + str(card5[0]) + "\n")

        # Calculate the players current score
        calculateTotal = calculateCurrentScore(playerTotal, card5[1], playerAceCounter)
        playerTotal = int(calculateTotal[0])
        playerAceCounter = int(calculateTotal[1])
        print("Player's Current Total = " + str(playerTotal) + "\n")

        # Track how many cards you've drawn
        cardsUsed = int(cardsUsed + 1)

        # Check if your total score is 21 or greater
        if playerTotal < 21:
            # Ask what the player would like to do next
            returnedActions = hitOrStand(firstAction)
            nextAction = returnedActions[0]
            firstAction = returnedActions[1]
        else:
            nextAction = 2
    elif nextAction == 3:
        # Print the players 3 cards
        print("\nPLAYER\n")
        print("Card 1 | " + str(card3[0]))
        print("Card 2 | " + str(card4[0]))
        print("Card 3 | " + str(card5[0]) + "\n")

        # Calculate the players current score
        calculateTotal = calculateCurrentScore(playerTotal, card5[1], playerAceCounter)
        playerTotal = int(calculateTotal[0])
        playerAceCounter = int(calculateTotal[1])
        print("Player's Current Total = " + str(playerTotal) + "\n")

        # Track how many cards you've drawn
        cardsUsed = int(cardsUsed + 1)

        # Force you to hold
        nextAction = 2

    # Continue the game based on the players input
    if nextAction == 1:
        # Print the players 3 cards
        print("\nPLAYER\n")
        print("Card 1 | " + str(card3[0]))
        print("Card 2 | " + str(card4[0]))
        print("Card 3 | " + str(card5[0]))
        print("Card 4 | " + str(card6[0]) + "\n")

        # Calculate the players current score
        calculateTotal = calculateCurrentScore(playerTotal, card6[1], playerAceCounter)
        playerTotal = int(calculateTotal[0])
        playerAceCounter = int(calculateTotal[1])
        print("Player's Current Total = " + str(playerTotal) + "\n")

        # Track how many cards you've drawn
        cardsUsed = int(cardsUsed + 1)

        # Check if your total score is 21 or greater
        if playerTotal < 21:
            # Ask what the player would like to do next
            returnedActions = hitOrStand(firstAction)
            nextAction = returnedActions[0]
            firstAction = returnedActions[1]
        else:
            nextAction = 2

    # Continue the game based on the players input
    if nextAction == 1:
        # Print the players 3 cards
        print("\nPLAYER\n")
        print("Card 1 | " + str(card3[0]))
        print("Card 2 | " + str(card4[0]))
        print("Card 3 | " + str(card5[0]))
        print("Card 4 | " + str(card6[0]))
        print("Card 5 | " + str(card7[0]) + "\n")

        # Calculate the players current score
        calculateTotal = calculateCurrentScore(playerTotal, card7[1], playerAceCounter)
        playerTotal = int(calculateTotal[0])
        playerAceCounter = int(calculateTotal[1])
        print("Player's Current Total = " + str(playerTotal) + "\n")

        # Track how many cards you've drawn
        cardsUsed = int(cardsUsed + 1)

    #? End the game and calculate the dealers score if need be

    # Check if your total score is greater than 21, 21 or less than 21
    if playerTotal > 21:
        print("YOU'RE BUST!\n")
        print("\nPlayer's Current Total = " + str(playerTotal) + "\nThis means you've gone bust... \n\nsorry!\n")
        validExit = playAgain(validExit)
    elif playerTotal == 21:
        print("YOU'VE GOT A BLACK JACK!\n")
        print("\nPlayer's Current Total = " + str(playerTotal) + "\nThis means you've got a Black Jack!... \n\nWell Done!\n")
        validExit = playAgain(validExit)
    else:
        print("\nPlayer's Final Total = " + str(playerTotal) + "!\n")

        # Reset cards used variable
        cardsUsed = int(0)

        # Calculate the dealers score
        calculateTotal = calculateCurrentScore(dealerTotal, card1[1], dealerAceCounter)
        calculateTotal = calculateCurrentScore(calculateTotal[0], card2[1], calculateTotal[1])

        # Modifed cards used variable accordingly
        cardsUsed = int(cardsUsed + 2)

        # Check the dealers score & add more cards accordingly
        if calculateTotal[0] < 17:
            calculateTotal = calculateCurrentScore(calculateTotal[0], card8[1], calculateTotal[1])
            cardsUsed = int(cardsUsed + 1)
        if calculateTotal[0] < 17:
            calculateTotal = calculateCurrentScore(calculateTotal[0], card9[1], calculateTotal[1])
            cardsUsed = int(cardsUsed + 1)
        if calculateTotal[0] < 17:
            calculateTotal = calculateCurrentScore(calculateTotal[0], card10[1], calculateTotal[1])
            cardsUsed = int(cardsUsed + 1)

        # Store the dealers score in vairables
        dealerTotal = int(calculateTotal[0])
        dealerAceCounter = int(calculateTotal[1])

        # Print the dealers hand
        print("FINAL DEALER HAND!\n")
        if cardsUsed >= 1:
            print("Card 1 | " + str(card1[0]))
        if cardsUsed >= 2:
            print("Card 2 | " + str(card2[0]))
        if cardsUsed >= 3:
            print("Card 3 | " + str(card8[0]))
        if cardsUsed >= 4:
            print("Card 4 | " + str(card9[0]))
        if cardsUsed >= 5:
            print("Card 5 | " + str(card10[0]))
        print("\nDealer's Final Total = " + str(dealerTotal) + "!")
    
        # Compareing the player score against the dealer score
        if dealerTotal > 21:
            print("\nYOU WIN!\nThe dealer went bust!\n")
        else:
            if playerTotal < dealerTotal:
                print("\nYOU LOST!\nSorry!\n")
            elif playerTotal == dealerTotal:
                print("\nIT'S A DRAW!\nNo one wins!\n")
            else:
                print("\nYOU WIN!\nWell Done!\n")
        
        validExit = playAgain(validExit)

#TODO Finish optimizing the code
#TODO Add in the scoring system to make this a proper game.
#TODO Maybe add in the read and write feature to save the users score.