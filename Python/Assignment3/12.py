''' 12. Write a program that generate two random numbers. If the total of the two dices is 7 or 11, print "You win!". Otherwise, print "Try again!".'''

import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2


total = roll_dice()
if total == 7 or total == 11:
    print("You win!")
else:
    print("Try again!")
