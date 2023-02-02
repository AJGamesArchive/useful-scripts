# Importing the random library
import random

# Declare the 2 lists of people and the final list of pairs
gifters = []
receivers = []
finalPairs = []

# Function that asks the user to enter who is taking part in Secret Santa
def enterParticipants():
    validEntry = False
    participantName = str(input("\nPlease enter who is participating one at a time and type `Done` when finished.\n: "))
    while not validEntry:
        if participantName == "Done" or participantName == "done" or participantName == "DONE":
            validEntry = True
        else:
            gifters.append(participantName)
            receivers.append(participantName)
            participantName = str(input(": "))

# Function that generates the gifting pairs
def pairGenerater():
    pairCounter = int(0)
    while gifters and receivers:
        firstPerson = str(random.choice(gifters))
        secondPerson = str(random.choice(receivers))
        if firstPerson is not secondPerson:
            pair = str(f"{firstPerson} ----> {secondPerson}")
            pairCounter = int(pairCounter + 1)
            finalPairs.append(f"Pair: {str(pairCounter)}")
            finalPairs.append(pair)
            gifters.remove(firstPerson)
            receivers.remove(secondPerson)

# Declaring main validation FLAG
validExit = False

while not validExit:
    # Clearing all the pairs from the final list of pairs
    finalPairs = []
    # Declaring validation FLAG
    validFinished = False
    # Runs the program
    print("\nWelcome to the Secret Santa generater!")
    enterParticipants()
    print(f"\nThe people participating are: \n{gifters}")
    pairGenerater()
    print(f"\nThe pairs for Secret Santa are as follows:\n{finalPairs}")
    # Asking if the user is done
    while not validFinished:
        finished = str(input("\nAre you finished? (Y/N) \n: ").lower())
        if finished == "y" or finished == "yes":
            validFinished = True
            validExit = True
            with open("Secret Santa Pairs.txt", "w") as f:
                f.write("")
                for item in finalPairs:
                    f.writelines(f"{str(item)}\n")
            print("\nSuccessfully outputted pairs to a text file!")
        elif finished == "n" or finished == "no":
            validFinished = True
        else:
            print("\nPlease enter either Yes or No.")

#TODO Replace while loop with function