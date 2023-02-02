# Valid Symbols
validSymbols = ("!", "&", "%", "+", "=", "*")

# Validation FLAGS
validPassword = False

# Declaring password variable so it's global
password = str("")
passwordLength = int(0)

# Enter and validate a password
while not validPassword:
  # Ask user for input and calculate the length of the entered password
  password = str(input("Please enter a password: "))
  passwordLength = len(password)
  # Validate the length of the entered password
  if passwordLength >= 8 and passwordLength <= 15:
    # Declare validation FLAG
    invalidSymbols = False
    # Check for invalid characters within the password
    for letter in password:
      if not letter.isalpha() and not letter.isdigit() and not letter in validSymbols:
        # Invalid characters found
        invalidSymbols = True
    # If invalid characters are found, ask the user to re-enter the password with valid characters
    if invalidSymbols == True:
      print(f"Some symbols you have entered are not valid! Please enter a password that only uses {validSymbols}")
    else:
      # If no invalid characters, accept the password and break the loop
      validPassword = True
  # Tell the user whether the entered password is to short or to long
  elif passwordLength < 8:
    print("Your password is too short! Please enter a valid password.")
  else:
    print("Your password is too long! Please enter a valid password.")

# Declaring counters
lowerCounter = int(0)
upperCounter = int(0)
numberCounter = int(0)
symbolCounter = int(0)

# Count number of lower case letters in password
for letter in password:
  if letter.islower():
    lowerCounter = int(lowerCounter + 1)

# Count number of upper case letters in password
for letter in password:
  if letter.isupper():
    upperCounter = int(upperCounter + 1)

# Count number of numbers in password
for letter in password:
  if letter.isdigit():
    numberCounter = int(numberCounter + 1)

# Count number of symbols in password
for letter in password:
  if letter in validSymbols:
    symbolCounter = int(symbolCounter + 1)

# Declaring score break down variables
lowerCaseScore = int(lowerCounter * 5)
upperCaseScore = int(upperCounter * 5)
numberScore = int(numberCounter * 10)
symbolScore = int(symbolCounter * 10)
minusScore = int(0)

# Declaring total score counter
score = int(lowerCaseScore + upperCaseScore + numberScore + symbolScore)

# Calculating bonus points for password length
if passwordLength >= 10:
  lengthScore = int(20)
  score = int(score + 20)
else:
  lengthScore = int(0)

# Subtracting points if the whole password is lowercase
if password.islower():
  minusScore = int(passwordLength * 3)
  score = int(score - minusScore)

# Subtracting points if the whole password is uppercase
if password.isupper():
  minusScore = int(passwordLength * 3)
  score = int(score - minusScore)

# Subtracting points if the whole password contains numbers
if password.isdigit():
  minusScore = int(passwordLength * 5)
  score = int(score - minusScore)

# Calculating the strength of the password
if score <= 20:
  rating = str("Very Weak")
elif score >= 21 and score <= 40:
  rating = str("Weak")
elif score >= 41 and score <= 70:
  rating = str("Okay")
elif score >=71 and score <= 80:
  rating = str("Strong")
else:
  rating = str("Very Strong")

# Outputting all the calculated data
print("The password is a good length.")
print("The password uses valid symbols.")
print(f"Lower Case Score: {lowerCaseScore}")
print(f"Upper Case Score: {upperCaseScore}")
print(f"Number Score: {numberScore}")
print(f"Symbol Score: {symbolScore}")
print(f"Password Length Bonus: {lengthScore}")
print(f"Points Lost Due To Consistent Characters: {minusScore}")
print(f"Total Score: {score}")
print(f"\nThe password: {password} is: {rating}!")