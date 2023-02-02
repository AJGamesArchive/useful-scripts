validBase = bool(False)
validNew = bool(False)
validAmount = bool(False)

conversations = dict({
    "1 - British Pond": [1.00, "£"],
    "2 - Euro": [1.18, "€"],
    "3 - US Dollar": [1.25, "$"],
})

while not validBase:
    print("Please select a base currency by entering the corresponding number.")
    print(*conversations.keys(), sep="\n")
    data = str(input(": "))
    if data == "1":
        originalSelection = str("1")
        baseCurrency = str("1 - British Pond")
        validBase = bool(True)
    elif data == "2":
        originalSelection = str("2")
        baseCurrency = str("2 - Euro")
        validBase = bool(True)
    elif data == "3":
        originalSelection = str("3")
        baseCurrency = str("3 - US Dollar")
        validBase = bool(True)
    else:
        print("Please enter a valid number.")

while not validNew:
    print("Please select a currency to convert to by entering the corresponding number.")
    print(*conversations.keys(), sep="\n")
    data = str(input(": "))
    if data == originalSelection:
        print("You cannot convert an amount to the same currency you started with. Please select a different currency.")
    else:
        if data == "1":
            newCurrency = str("1 - British Pond")
            validNew = bool(True)
        elif data == "2":
            newCurrency = str("2 - Euro")
            validNew = bool(True)
        elif data == "3":
            newCurrency = str("3 - US Dollar")
            validNew = bool(True)
        else:
            print("Please enter a valid number.")

while not validAmount:
    try:
        data = float(input("Please enter the amount you wish to convert: "))
    except ValueError:
        print("Please enter a valid amount.")
    else:
        amount = float(round(data, 2))
        validAmount = True

if baseCurrency == "1 - British Pond":
    exchange = float(conversations[newCurrency][0])
    convertedAmount = float(round(amount * exchange, 2))
    currencySymbol = str(conversations[newCurrency][1])
    print(f"The new amount is {str(currencySymbol)} {str(convertedAmount)}")
else:
    baseExchange = float(conversations[baseCurrency][0])
    newExchange = float(conversations[newCurrency][0])
    exchange = float(round(newExchange / baseExchange, 2))
    convertedAmount = float(round(amount * exchange, 2))
    currencySymbol = str(conversations[newCurrency][1])
    if newCurrency is not "1 - British Pond":
        finalConversion = float(round(convertedAmount * newExchange, 2))
    print(f"The new amount is {str(currencySymbol)} {str(convertedAmount)}")

#TODO Replace all the while loops with functions