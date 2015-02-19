#CoinToss.py
#by Ryan Rueber
#Simulates a number of coin tosses

#import statements
import random
from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox

#Create a window
root = Tk()
w = Label(root, text="Coin Toss Test")
w.pack()

# initialize variables
heads = 0   # number of heads
tails = 0   # number of tails
flips = 0   # how many flips (user decides)
toss = 0    # result of each coin toss
messagebox.showinfo("welcome",
                    "We're going to simulate a number " + \
                    "of coin tosses. You decide how " + \
                    "many tosses, and I'll show you "
                    "how many heads and how many tails " + \
                    "you flipped")

# Get number of loops from user
flips = simpledialog.askinteger("How Many Tosses?",
                                "How many times do you" +\
                                "want to flip a coin?")
# loop [flips] times
count = 0
while count < flips:
    toss = random.randint(1,2)# 1 is heads, 2 is tails
    if toss == 1:
        heads += 1
    if toss == 2:
        tails += 1
    count += 1
messagebox.showinfo("Results", "Out of {} flips, there were {} heads, and {} tails".format(flips, heads, tails))
    #Check to see if toss is heads (1) or tails (2)
    # if it's 1, add 1 to heads
    #if it's 2, add 1 to tails

    #add 1 to counter

# PRINT out of {flips} loops,
# there were {heads}, and {tails} tails.

#For bonus, give us the % of heads and % of tails
# Close the window & clean up
root.destroy()