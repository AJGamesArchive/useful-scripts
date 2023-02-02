import random
from fractions import Fraction

def additionAndSubtraction(amount: int):
    for number in range(amount):
        print(f"Generating question {number + 1}")
        validQuestion = bool(False)
        applicableOpts = tuple(("+", "-"))
        while not validQuestion:
            firstNum = int(random.choice(range(1, 100)))
            secondNum = int(random.choice(range(1, 100)))
            operation = str(random.choice(applicableOpts))
            match operation:
                case "+":
                    answer = int(firstNum + secondNum)
                    question = str(f"{str(firstNum)} + {str(secondNum)} = ___")
                    equation = str(f"{str(firstNum)} + {str(secondNum)} = {str(answer)}")
                case "-":
                    answer = int(firstNum - secondNum)
                    question = str(f"{str(firstNum)} - {str(secondNum)} = ___")
                    equation = str(f"{str(firstNum)} - {str(secondNum)} = {str(answer)}")
                case _:
                    continue
            if answer < 0:
                continue
            if equation in answers:
                continue
            validQuestion = bool(True)
        questions[f"Question {str(number + 1)}"] = str(question)
        answers[f"Question {str(number + 1)}"] = str(equation)

def multiplicationAndDivision(amount: int):
    for number in range(amount):
        print(f"Generating question {number + 1}")
        validQuestion = bool(False)
        applicableOpts = tuple(("x", "/"))
        while not validQuestion:
            firstNum = int(random.choice(range(1, 12)))
            secondNum = int(random.choice(range(1, 12)))
            operation = str(random.choice(applicableOpts))
            answer = int(firstNum * secondNum)
            if answer < 0:
                continue
            match operation:
                case "x":
                    question = str(f"{str(firstNum)} x {str(secondNum)} = ___")
                    equation = str(f"{str(firstNum)} x {str(secondNum)} = {str(answer)}")
                case "/":
                    question = str(f"{str(answer)} / {str(secondNum)} = ___")
                    equation = str(f"{str(answer)} / {str(secondNum)} = {str(firstNum)}")
                case _:
                    continue
            if equation in answers:
                continue
            validQuestion = bool(True)
        questions[f"Question {str(number + 1)}"] = str(question)
        answers[f"Question {str(number + 1)}"] = str(equation)

def fractions(amount: int):
    for number in range(amount):
        print(f"Generating question {number + 1}")
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
                question = str(f"{str(numFirst)}/{str(denumFirst)} + {str(numSecond)}/{str(denumSecond)} = ___")
                equation = str(f"{str(numFirst)}/{str(denumFirst)} + {str(numSecond)}/{str(denumSecond)} = {str(answer)}")
            elif operation == "-":
                denum = int(denumFirst * denumSecond)
                newNumFirst = int(numFirst * denumSecond)
                newNumSecond = int(numSecond * denumFirst)
                num = int(newNumFirst - newNumSecond)
                numCheck = str(num)
                if not numCheck.isdigit():
                    continue
                answer = Fraction(num,denum)
                question = str(f"{str(numFirst)}/{str(denumFirst)} - {str(numSecond)}/{str(denumSecond)} = ___")
                equation = str(f"{str(numFirst)}/{str(denumFirst)} - {str(numSecond)}/{str(denumSecond)} = {str(answer)}")
            elif operation == "x":
                num = int(numFirst * numSecond)
                denum = int(denumFirst * denumSecond)
                answer = Fraction(num,denum)
                question = str(f"{str(numFirst)}/{str(denumFirst)} x {str(numSecond)}/{str(denumSecond)} = ___")
                equation = str(f"{str(numFirst)}/{str(denumFirst)} x {str(numSecond)}/{str(denumSecond)} = {str(answer)}")
            else:
                num = int(numFirst * denumSecond)
                denum = int(denumFirst * numSecond)
                answer = Fraction(num,denum)
                question = str(f"{str(numFirst)}/{str(denumFirst)} / {str(numSecond)}/{str(denumSecond)} = ___")
                equation = str(f"{str(numFirst)}/{str(denumFirst)} / {str(numSecond)}/{str(denumSecond)} = {str(answer)}")
            if equation in answers:
                continue
            validQuestion = bool(True)
        questions[f"Question {str(number + 1)}"] = str(question)
        answers[f"Question {str(number + 1)}"] = str(equation)

questions = dict({})
answers = dict({})

validType = bool(False)
validAmount = bool(False)

questionType = int(0)
questionAmount = int(0)

while not validType:
    print("\nSelect a type of question to generate.\n1 - Addition & Subtraction\n2 - Multiplication & Division\n3 - Fractions")
    data = str(input("\n: "))
    match data:
        case "1":
            questionType = int(1)
            validType = bool(True)
        case "2":
            questionType = int(2)
            validType = bool(True)
        case "3":
            questionType = int(3)
            validType = bool(True)
        case _:
            print("Please enter a valid number.")

while not validAmount:
    data = str(input("\nHow many questions would you like?\n: "))
    if data.isdigit():
        questionAmount = int(data)
        validAmount = bool(True)
    else:
        print("Please enter a number.")

match questionType:
    case 1:
        additionAndSubtraction(questionAmount)
    case 2:
        multiplicationAndDivision(questionAmount)
    case 3:
        fractions(questionAmount)
    case _:
        print("An unsuspected error has occurred! Please try again.")
        exit()

with open("Questions.txt", "w") as q:
    q.write("")
    for key, value in questions.items():
        q.writelines(f"{str(key)}\n {str(value)}\n\n")

with open("Answers.txt", "w") as a:
    a.write("")
    for key, value in answers.items():
        a.writelines(f"{str(key)}\n {str(value)}\n\n")

print("\nSuccessfully outputted questions and answers to a text file.\n")