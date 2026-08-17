import sys
import random
from enum import Enum


def rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input("\nEnter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n")
    print("")
    if playerchoice not in ["1", "2", "3"]:
        print("Please enter between 1 and 3.")
        return rps()

    player = int(playerchoice)

    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace("RPS.", ""))
    print("Computer chose " + str(RPS(computer)).replace("RPS.", "") + "\n")

    if player == 1 and computer == 3:
        print("🍕 You win !!")
    elif player == 2 and computer == 1:
        print("🍕 You win !!")
    elif player == 3 and computer == 2:
        print("🍕 You win !!")
    elif player == computer:
        print("😲 Tie game !!")
    else:
        print("🐍 Python wins !!")

    while True:
        playagain = input("\nPlay again ?\nY for Yes or Q for Quit\n\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return rps()
    else:
        sys.exit("\n👌 Bye !!\n")


rps()
