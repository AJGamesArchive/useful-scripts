import random
import string

alphabet = string.ascii_letters
digits = string.digits
symbols = ["!", "?", "%", "&"]

choice = "12"

token = ""

for i in range(100):
  selection = random.choice(choice)
  match selection:
    case "1":
      char = random.choice(alphabet)
    case "2":
      char = random.choice(digits)
    case "3":
      char = random.choice(symbols)
  token = token + char

print(token)

#TODO Turn into a single function