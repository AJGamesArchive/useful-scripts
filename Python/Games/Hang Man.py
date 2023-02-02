# Library imports
import random
import requests

# Get a list of random words
site = str("https://www.mit.edu/~ecprice/wordlist.10000")
wordList = requests.get(site)
generatedWords = wordList.content.decode().splitlines()

# Pre-set words
testWords = list([
  "galaxy",
])

# Declare list for incorrect characters
incorrectChar = list([])

# Validation FLAG decelerations
validMenuSelection = bool(False)
validWord = bool(False)
validWin = bool(False)
validData = bool(False)

# Asking the user what they would like to do
while not validMenuSelection:
  selection = str(input("\nWhat would you like to do?\n1 - Enter Custom Word\n2 - Generate Random Word\n\n: "))
  match selection:
    case "1":
      validMenuSelection = bool(True)
      while not validWord:
        word = str(input("\nPlease enter a word: ").upper())
        if word.isalpha():
          validWord = bool(True)
        else:
          print("\nPlease enter a word that only contains letters.")
          continue
    case "2":
      word = str(random.choice(generatedWords).upper())
      validMenuSelection = bool(True)
    case _:
      print("\nPlease enter either 1 or 2.")
      continue

# Hide Word print shoving #! Temporary fix, replace with file reading later
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

# Get length of word
wordLen = int(len(word))

# Declare answer string
answer = str("")

# Make the answer string the length of the word
for i in range(wordLen):
  answer = str("".join((answer, "_")))

# DDeclaring counters
roundCount = int(0)
strikes = int(10)

# Main game loop
while not validWin:
  roundCount = int(roundCount + 1)
  print(f"\nGUESS {str(roundCount)}\n\n{str(answer)}\n\nStrikes remaining: {str(strikes)}\nLetters Guessed: {str(incorrectChar)}")
  while not validData:
    data = str(input("\nGuess a letter: ").upper())
    if data.isalpha() and len(data) == 1 and not data in incorrectChar and not data in answer:
      print(data)
      validData = bool(True)
    else:
      print("Please enter a single letter that you have not guessed before.")
      continue
  validData = bool(False)
  charPos = list([])
  if data in word:
    for pos, char in enumerate(word):
      if char == data:
        charPos.append(pos)
    for i in charPos:
      answer = answer[:i] + data + answer[i+1:]
  else:
    print("\nThat letter is not in the word!")
    incorrectChar.append(data)
    strikes = int(strikes - 1)
  if answer == word:
    print(f"\nWell Done!\n\nYou have correctly guessed the word {str(answer)} with {str(strikes)} strikes left.\n")
    validWin = bool(True)
  else:
    match strikes:
      case 0:
        print(f"\nSorry, you have run out of strikes. The word was:\n\n{str(word)}\n")
        validWin = bool(True)
      case _:
        continue