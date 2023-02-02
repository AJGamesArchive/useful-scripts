# Library imports
from tkinter import *
from tkinter import ttk
import random

# Declaring global variables
counter = int(1)
targetNumber = int(random.randint(1, 100))

# Submit button function
def enterNumber():
    global messageLbl
    global counter
    number = str(inputEntry.get())
    if number.isdigit():
        number = int(number)
        if number >= 1 and number <= 100:
            if number == targetNumber:
                messageLbl.config(text=f"Correct! The Number was {str(number)}!")
            elif number < targetNumber:
                messageLbl.config(text="You need to guess Higher!")
                counter = int(counter + 1)
                roundNumberLbl.config(text=f"ROUND {counter}")
            else: 
                messageLbl.config(text="You need to guess Lower!")
                counter = int(counter + 1)
                roundNumberLbl.config(text=f"ROUND {counter}")
        else:
            messageLbl.config(text="Please enter a whole number between 1 and 100!")
    else:
        messageLbl.config(text="Please enter a whole number between 1 and 100!")

# Reset button function
def reset():
    global targetNumber
    global counter
    targetNumber = int(random.randint(1, 100))
    messageLbl.config(text="Successfully Reset!")
    counter = int(1)
    roundNumberLbl.config(text=f"ROUND {counter}")

# Initializing the main application window
application = Tk()
application.geometry("540x350")
application.resizable(0,0)
application.title("Higher Or Lower?")

# Setting up the grid that the GUI will be built on
frame = ttk.Frame(application, padding="10").grid()

# Adding GUI elements to the grid system
welcomeLbl = ttk.Label(
    frame,
    text="Welcome to Higher or Lower!",
    font=("Aerial 16 bold"),
    padding=5
).grid(column=0, row=0, columnspan=3)

infoLbl = ttk.Label(
    frame,
    text="Try to guess the randomly generated number in the fewest amount of rounds.",
    font=("Aerial 12"),
    background="teal",
    padding=5,
).grid(column=0, row=1, columnspan=3)

roundNumberLbl = ttk.Label(
    frame,
    text=f"ROUND {counter}",
    font=("Aerial 12 bold"),
    padding=5
)
roundNumberLbl.grid(column=0, row=2, columnspan=3)

questionLbl = ttk.Label(
    frame,
    text="Enter a number between 1 and 100:",
    font=("Aerial 12 italic"),
    padding=5
).grid(column=0, row=3, columnspan=3)

inputEntry = ttk.Entry()
inputEntry.grid(column=0, row=4, columnspan=3)

messageLbl = ttk.Label(
    frame,
    text="Awaiting Input...",
    font="Aerial 12 bold",
    padding=5   
)
messageLbl.grid(column=0, row=5, columnspan=3)

submitBtn = ttk.Button(
    frame,
    text="Submit",
    padding=5,
    command=enterNumber
).grid(column=0, row=6, sticky="e")

resetBtn = ttk.Button(
    frame,
    text="Reset",
    padding=5,
    command=reset
).grid(column=1, row=6)

exitBtn = ttk.Button(
    frame,
    text="Exit",
    padding=5,
    command=application.destroy
).grid(column=2, row=6, sticky="w")

# Running the GUI application
application.mainloop()