import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True
print("")
while playagain:
    playerchoice = input("Enter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n")
    player = int(playerchoice)
    print("")
    if player < 1 or player > 3:
        print("Please enter 1, 2 or 3 only:\n")
        continue
    computerchoice = random.choice("123")
    computer = int(computerchoice)
    print("You chose: " + str(RPS(player)).replace("RPS.", ""))
    print("Computer chose: " + str(RPS(computer)).replace("RPS.", ""))
    print("")
    if player == 1 and computer == 3:
        print("🍕 You win !!!")
    elif player == 2 and computer == 1:
        print("🍕 You win !!!")
    elif player == 3 and computer == 2:
        print("🍕 You win !!!")
    elif player == computer:
        print("😲 Tie game !!!")
    else:
        print("🐍 Python wins !!!")
    print("")
    playagain_choice = input("Play again ?\nY for Yes or any other key to quit.\n\n")
    if playagain_choice.lower() == "y":
        continue
    else:
        print("")
        playagain = False
sys.exit("Bye !\n")
