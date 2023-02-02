# Imports
import random

# Main Functions
def gameModeOne():
  runningGameOne = bool(True)
  print("\nAll of these questions will give you answers that are whole percentages.")
  score = int(0)
  questionNum = int(0)
  while runningGameOne:
    questionNum = int(questionNum + 1)
    print(f"\nQUESTION {str(questionNum)} OF 10!")
    question, answer, numAnswer = conversationQuestionGen()
    print(question)
    validAnswer = bool(False)
    while not validAnswer:
      inputAnswer = str(input("\nEnter your answer as a whole number without the percent sign.\n: "))
      if inputAnswer.isdigit():
        inputAnswer = int(inputAnswer)
        validAnswer = bool(True)
      else:
        print("\nPlease enter a whole percentage without the percent sign.")
        continue
    if inputAnswer == numAnswer:
      score = int(score + 1)
      print(f"\nCORRECT! The answer was {str(numAnswer)}%.\n+ 1 Point\n\nCurrent Score: {str(score)}")
    else:
      print(f"\nINCORRECT! The answer was: \n{str(answer)}\n\nCurrent Score: {str(score)}")
    data = str(input("\n: "))
    match questionNum:
      case 10:
        runningGameOne = bool(False)
      case _:
        continue

def gameModeTwo():
  runningGameTwo = bool(True)

# Generator Functions
def conversationQuestionGen():
  validQuestion = bool(False)
  while not validQuestion:
    numerator = random.choice(range(1, 23))
    denominator = random.choice(range(2, 24))
    if numerator >= denominator:
      continue
    numAnswer = float((numerator / denominator) * 100)
    if not numAnswer > 0 or not numAnswer < 100 or not numAnswer.is_integer():
      continue
    numAnswer = int(numAnswer)
    question = str(f"\nConvert the following Fraction into a Percentage.\n\n{str(numerator)}/{str(denominator)} = __%")
    answer = str(f"\n{str(numerator)}/{str(denominator)} = {str(numAnswer)}%")
    validQuestion = bool(True)
  return question, answer, numAnswer

def percentageQuestionGen():
  validQuestion = bool(False)

# FLAGS
running = bool(True)

# Main Loop
while running:
  modeSelect = str(input("\nSelect a game mode.\n1 - Convert Fractions To Percentages\n2 - Calculate A Percentage Of A Number\n3 - Exit\n\n: "))
  match modeSelect:
    case "1":
      gameModeOne()
      continue
    case "2":
      gameModeTwo()
      continue
    case "3":
      running = bool(False)
    case _:
      print("\nPlease enter either 1 or 2.")
      continue
