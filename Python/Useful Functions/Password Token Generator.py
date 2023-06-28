import random
import string

def passwordGenerator():
  alphabet = string.ascii_letters
  digits = string.digits
  symbols = ["!", "?", "%", "&"]
  choice = "12"
  token = ""
  for i in range(20):
    selection = random.choice(choice)
    if selection == "1":
      char = random.choice(alphabet)
    if selection == "2":
      char = random.choice(digits)
    if selection == "3":
      char = random.choice(symbols)
    token = token + char

print(passwordGenerator)
