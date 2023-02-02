import random

correct = False
counter = int(1)
targetNumber = int(random.randint(1, 100))

def enterNumber():
    validNumber = False
    while not validNumber:
        number = str(input("Please enter a whole number between 1 and 100: "))
        if number.isdigit():
            number = int(number)
            if number >= 1 and number <= 100:
                validNumber = True
            else:
                print("Please enter a whole number between 1 and 100.")
        else:
            print("Please enter a whole number between 1 and 100.")
    return int(number)

def targetChecker(targetNumber: int, number: int):
    if number == targetNumber:
        message = str(f"You are Correct! The number was {str(number)}.")
        result = True
    elif number < targetNumber:
        message = str("You need to guess Higher!")
        result = False
    else: 
        message = str("You need to guess Lower!")
        result = False
    results = (message, result)
    return results

while not correct:
    print(f"ROUND {str(counter)}!")
    number = enterNumber()
    results = targetChecker(targetNumber, number)
    message = str(results[0])
    finished = bool(results[1])
    print(message)
    if not finished:
        counter = int(counter + 1)
    else:
        print("Well Done!")
        correct = True