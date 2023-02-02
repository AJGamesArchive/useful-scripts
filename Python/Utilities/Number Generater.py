# Imports the "random" library
import random

# Declearing the validation variable (FLAG)
validRepeat = False

while not validRepeat:
    # Declearing repeatable validationvariables (FLAGS)
    validMin = False
    validMax = False

    # Ask the user for a minimum number
    while not validMin:
        min = str(input("\nPlease enter then minimum number that can be generated: "))
        if min.isdigit():
            min = int(min)
            validMin = True
        else:
            print("Please enter a whole number!")

    # Ask the user for a maximum number
    while not validMax:
        max = str(input("\nPlease enter the maximum number that can be generated: "))
        if max.isdigit():
            max = int(max)
            validMax = True
        else:
            print("Please enter a whole number!")

    # Generate a number based on given paramaters and then print it
    number = int(random.randint(min, max))
    print("\nHere is your number: " + str(number))

    # Ask the user if they would like to generate another number
    repeat = str(input("\nWould you like to generate another number? (Y/N): ").lower())

    # Either restart the program or exit the program depending on the given paramaters
    if repeat == "yes" or repeat == "y":
        print("\nRestarting...")
    else:
        validRepeat = True

#TODO Replace all the while loops with functions