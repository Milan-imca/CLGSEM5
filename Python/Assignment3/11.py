'''11. Write a Python script that uses the random package to simulate the rolling of two six-sided dice'''
import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2


dice1, dice2 = roll_dice()
print(f"Die 1: {dice1}, Die 2: {dice2}, Total: {dice1 + dice2}")
