# Importing the "math" library
import math

# Declare main validation FLAG
validExit = False

# Printing the starting message
print("\nThis calculator can answer 2 number calculations that are: Addition, Subtraction, Multiplication, Division, To The Power To, or Square Root. \nPlease enter your calculation!\n")

# Tuple of applicable operations
applicableOps = ("+", "-", "*", "/", "**", "add", "subtracked", "multiply", "divide", "to the power to", "square root")

# Print to enterable operations
print("The applicable operations you can enter into this calculator are as follows:\n" + str(applicableOps) + "\n")

while not validExit:
    # Setting up validation variables (Flags)
    validFirstNum = False
    validOperation = False
    validSecondNum = False
    validRetry = False

    # Asking the user for their calculation
    while not validFirstNum:
        try:
            firstNum = float(input("Please enter the first number in your calculation: "))
        except ValueError:
            print("Please enter a number!")
        else:
            validFirstNum = True

    while not validOperation:
        operation = str(input("Please enter the operation your calculation needs: ").lower())
        if operation in applicableOps:
            validOperation = True
        else:
            print("Please enter a valid operation such as: " + str(applicableOps))

    if operation == "square root":
        print("\nCalculating...\n")
    else:
        while not validSecondNum:
            try:
                secondNum = float(input("Please enter the second number in your calculation: "))
            except ValueError:
                print("Please enter a number!")
            else:
                validSecondNum = True

    match operation:
        case "+" | "add":
            answer = firstNum + secondNum
            operation = "+"
        case "-" | "subtracked":
            answer = firstNum - secondNum
            operation = "-"
        case "*" | "multiply":
            answer = firstNum * secondNum
            operation = "*"
        case "/" | "divide":
            answer = (firstNum / secondNum)
            operation = "/"
        case "square root":
            answer = math.sqrt(firstNum)
        case _:
            answer = firstNum ** secondNum
            operation = "**"

    # Printing the answer
    if operation == "square root":
        print("The square root of: " + str(firstNum) + " is: " + str(answer))
    else:
        print("\n" + str(firstNum) + " " + str(operation) + " " + str(secondNum) + " = " + str(answer) + "!")

    while not validRetry:
        retry = str(input("\nWould you like to do another calculation? (Y/N): ").lower())
        if retry == "yes" or retry == "y":
            print("\nRestarting...\n")
            validRetry = True
        else:
            validRetry = True
            validExit = True

#TODO Replace all the while loops with functions