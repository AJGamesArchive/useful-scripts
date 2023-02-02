import random
from fractions import Fraction

def questionGenerator():
    validQuestion = bool(False)
    while not validQuestion:
        numFirst = int(random.choice(range(1, 11)))
        denumFirst = int(random.choice(range(2, 12)))
        numSecond = int(random.choice(range(1, 11)))
        denumSecond = int(random.choice(range(2, 12)))
        if numFirst >= denumFirst:
            continue
        if numSecond >= denumSecond:
            continue
        if numFirst == numSecond and denumFirst == denumSecond:
            continue
        applicableOperations = list([
            "+",
            "-",
            "x",
            "÷",
        ])
        operation = str(random.choice(applicableOperations))
        if operation == "+":
            denum = int(denumFirst * denumSecond)
            newNumFirst = int(numFirst * denumSecond)
            newNumSecond = int(numSecond * denumFirst)
            num = int(newNumFirst + newNumSecond)
            answer = Fraction(num,denum)
            question = str(f"{str(numFirst)}/{str(denumFirst)} + {str(numSecond)}/{str(denumSecond)} = ?")
            if num < denum:
                message = str("Give your answer in it's simplest form.")
            else:
                message = str("Give your answer as an improper fraction in it's simplest form.")
        elif operation == "-":
            denum = int(denumFirst * denumSecond)
            newNumFirst = int(numFirst * denumSecond)
            newNumSecond = int(numSecond * denumFirst)
            num = int(newNumFirst - newNumSecond)
            numCheck = str(num)
            if not numCheck.isdigit():
                continue
            answer = Fraction(num,denum)
            question = str(f"{str(numFirst)}/{str(denumFirst)} - {str(numSecond)}/{str(denumSecond)} = ?")
            if num < denum:
                message = str("Give your answer in it's simplest form.")
            else:
                message = str("Give your answer as an improper fraction in it's simplest form.")
        elif operation == "x":
            num = int(numFirst * numSecond)
            denum = int(denumFirst * denumSecond)
            answer = Fraction(num,denum)
            question = str(f"{str(numFirst)}/{str(denumFirst)} x {str(numSecond)}/{str(denumSecond)} = ?")
            if num < denum:
                message = str("Give your answer in it's simplest form.")
            else:
                message = str("Give your answer as an improper fraction in it's simplest form.")
        else:
            num = int(numFirst * denumSecond)
            denum = int(denumFirst * numSecond)
            answer = Fraction(num,denum)
            question = str(f"{str(numFirst)}/{str(denumFirst)} ÷ {str(numSecond)}/{str(denumSecond)} = ?")
            if num < denum:
                message = str("Give your answer in it's simplest form.")
            else:
                message = str("Give your answer as an improper fraction in it's simplest form.")
        validQuestion = bool(True)
    return question, answer, message

def enterAnswer(question: str, message: str):
    validAnswer = bool(False)
    while not validAnswer:
        try:
            num, denum = map(str, str(input(f"Work out: \n\n{str(question)}\n\n{str(message)}\n\nEnter your answer in the form of number/number.\n: ")).split("/"))
        except ValueError:
            print("Please enter your answer as a fraction, in the form of number/number. Example: `1/2`.")
        else:
            if not num.isdigit():
                print("Please enter your answer as a fraction, in the form of number/number. Example: `1/2`.")
                continue
            if not denum.isdigit():
                print("Please enter your answer as a fraction, in the form of number/number. Example: `1/2`.")
                continue
            num = int(num)
            denum = int(denum)
            answer = Fraction(num,denum)
            validAnswer = bool(True)
    return answer

running = bool(True)
gameLog = dict({})
questionCounter = int(0)
score = int(0)

while running:
    validPlayAgain = bool(False)
    questionCounter = int(questionCounter + 1)
    print(f"\nQuestion: {questionCounter}\n")
    question, answer, message = questionGenerator()
    userAnswer = enterAnswer(question, message)
    gameLog[f"{questionCounter} Question"] = str(question)
    gameLog[f"{questionCounter} Conditions"] = str(message)
    gameLog[f"{questionCounter} Correct Answer"] = Fraction(answer)
    gameLog[f"{questionCounter} Your Answer"] = Fraction(userAnswer)
    if userAnswer == answer:
        print("\nThat is correct. Well done! +1 Point")
        score = int(score + 1)
        gameLog[f"{questionCounter} Result"] = str("Correct | +1")
    else:
        print(f"\nThat is not correct. The correct answer is: \n\n{str(question)}\n{str(answer)}")
        gameLog[f"{questionCounter} Result"] = str("Incorrect | +0")
    while not validPlayAgain:
        playAgain = str(input("\nWould you like to play again?\n: ").lower())
        match playAgain:
            case "y" | "yes":
                print(f"\nCurrent Score = {score}\n\nReloading...")
                validPlayAgain = bool(True)
            case "n" | "no":
                running = bool(False)
                print(f"Final Score = {score}")
                gameLog["Final Score"] = int(score)
                validPlayAgain = bool(True)
            case _:
                print("Please enter either Y or N.")

writeCounter = int(0)

with open("Game Log.txt", "w") as log:
    log.write("")
    for key, value in gameLog.items():
        writeCounter = int(writeCounter + 1)
        if writeCounter == 5:
            log.writelines(f"{str(key)} - {str(value)}\n\n")
            writeCounter = int(0)
        else:
            log.writelines(f"{str(key)} - {str(value)}\n")

print("successfully outputted game logs to a text file.")