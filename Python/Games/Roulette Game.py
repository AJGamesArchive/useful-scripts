# Import needed library's
import random

# Declaring retry validation FLAG
validPlayAgain = False

while not validPlayAgain:
    validGameOver = False
    money = 1000
    roundCounter = 1

    # Print what round number you're on
    print("\nROUND " + str(roundCounter) + "!\n\nThe aim of the game is to reach £2000 without going bankrupt!")

    # Main game loop
    while not validGameOver:

        # Declaring required variables and arrays
        validBet = False
        validMoneyBet = False
        bet = []
        colorBet = []
        betCounter = 5

        # Ask the user to place their money bet
        while not validMoneyBet:
            betMoney = str(input("\nYou currently have £" + str(money) + "!\n\nHow much money are you willing to bet? (Min bet of 10)\n: "))
            if betMoney.isdigit():
                betMoney = int(betMoney)
                if betMoney >= 10 and betMoney <= money:
                    validMoneyBet = True
                else:
                    print("Please enter an number between 10 and " + str(money) + "!")
            else:
                print("Please enter an number between 10 and " + str(money) + "!")

        # Asking the user to bet on what number & color the wheel will land on (The user can place 5 bets)
        while not validBet:
            validNumBet = False
            print("\nYou have " + str(betCounter) + " bets remaining!")
            betColor = str(input("\nWhich colour do you think the roulette wheel will land on? (1/2) \n1 = Black \n2 = Red \n\n: "))
            if betColor.isdigit():
                if betColor == "1" or betColor == "2":
                    if betColor == "1":
                        colorBet.append("Black")
                    elif betColor == "2":
                        colorBet.append("Red")
                    while not validNumBet:
                        enterBet = str(input("\nEnter the number from 1 to 32 that you think the roulette wheel will land on! \n: "))
                        if enterBet.isdigit():
                            enterBet = int(enterBet)
                            if enterBet >= 1 and enterBet <= 32:
                                bet.append(enterBet)
                                betCounter = int(betCounter) - 1
                                if betCounter == 0:
                                    validBet = True
                                validNumBet = True
                            else:
                                print("\nPlease enter a number between 1 and 32!")
                        else:
                            print("\nPlease enter a number between 1 and 32!")
                else:
                    print("\nPlease enter either 1 or 2!")
            else:
                print("\nPlease enter either 1 or 2!")

        # Setup your entered bets
        betOne = str(str(colorBet[0]) + " " + str(bet[0]))
        betTwo = str(str(colorBet[1]) + " " + str(bet[1]))
        betThree = str(str(colorBet[2]) + " " + str(bet[2]))
        betFour = str(str(colorBet[3]) + " " + str(bet[3]))
        betFive = str(str(colorBet[4]) + " " + str(bet[4]))

        # Randomly choose the color the roulette wheel has stopped on
        generateColor = ("Black", "Red")
        color = str(random.choice(generateColor))

        # Randomly choose the number the roulette wheel stopped on
        number = int(random.randint(1, 32))

        # Setup the roulette wheel results
        result = str(str(color) + " " + str(number))

        # Work out if you have won
        if betOne == result or betTwo == result or betThree == result or betFour == result or betFive == result:
            print("\nYour bets were:")
            print(str(betOne))
            print(str(betTwo))
            print(str(betThree))
            print(str(betFour))
            print(str(betFive))
            advance = str(input("\nPress any key to view the results!"))
            print("\nThe roulette wheel landed on:")
            print(str(result))
            print("\nYOU WON!")
            betMoney = int(int(betMoney) * 2)
            money = int(int(money) + int(betMoney))
            print("\nYou have won £" + str(betMoney) + "!\nYour new balance is £" + str(money) + "!")
            advance = str(input("\nPress any key to continue!"))
        else:
            print("\nYour bets were:")
            print(str(betOne))
            print(str(betTwo))
            print(str(betThree))
            print(str(betFour))
            print(str(betFive))
            advance = str(input("\nPress any key to view the results!"))
            print("\nThe roulette wheel landed on:")
            print(str(result))
            print("\nYOU LOST!")
            money = int(int(money) - int(betMoney))
            print("\nYou have lost £" + str(betMoney) + "!\nYour new balance is £" + str(money) + "!")
            advance = str(input("\nPress any key to continue!"))

        # Doing tracking stuff
        validRetry = False
        roundCounter = int(int(roundCounter) + 1)

        # Checking if you still have money left to play with
        if money >= 2000:
            print("\nCongratulations!\nYou have reached a higher balance then £10,000 and so you have won!")
            while not validRetry:
                retry = str(input("\nWould you like to play again? (Y/N): ").lower())
                if retry == "yes" or retry == "y":
                    print("\nRestarting...")
                    validRetry = True
                    validGameOver = True
                else:
                    print("\nExiting...\n")
                    validRetry = True
                    validGameOver = True
                    validPlayAgain = True
        elif money >= 10:
            print("\nROUND " + str(roundCounter) + "!")
        else:
            print("\nSorry, you do not have enough money to continue playing!")
            while not validRetry:
                retry = str(input("\nWould you like to play again? (Y/N): ").lower())
                if retry == "yes" or retry == "y":
                    print("\nRestarting...")
                    validRetry = True
                    validGameOver = True
                else:
                    print("\nExiting...\n")
                    validRetry = True
                    validGameOver = True
                    validPlayAgain = True