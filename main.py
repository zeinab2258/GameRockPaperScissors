import random
import winsound
from random import *


def errorSound():
    frequency = 1000  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)


def won(choice1, choice2):
    if choice1 == choice2:
        return 0
    if (choice1 == 's' and choice2 == 'p') or (choice1 == 'p' and choice2 == 'r') or (
            choice1 == 'r' and choice2 == 's'):
        return 1
    return 2


winPerson = 0
winComputer = 0

computerSelects = ['s', 'r', 'p']

while True:
    choicePerson = input('Type R/P/S For Rock/Paper/scissor:').lower()
    if choicePerson == 'r' or choicePerson == 'p' or choicePerson == 's':
        computerSelection = computerSelects[randint(0, 2)]
        print("computer Choice: " + computerSelection)
        if won(choicePerson, computerSelection) == 1:
            winPerson += 1
        if won(choicePerson, computerSelection) == 2:
            winComputer += 1
        print("computer= ", + winComputer)
        print("person= ", + winPerson)
    else:
        errorSound()
        print("invalid!!")
