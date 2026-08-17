import sys
import random
from enum import Enum


def rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input("\nEnter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("\nPlease enter number between 1, 2 or 3.")
        return rps()

    player = int(playerchoice)

    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("")
    print("You chose: " + str(RPS(player)).replace("RPS.", ""))
    print("Computer chose: " + str(RPS(computer)).replace("RPS.", ""))
    print("")

    if (
        (player == 1 and computer == 3)
        or (player == 2 and computer == 1)
        or (player == 3 and computer == 2)
    ):
        print("🍕 You win !!")
    elif player == computer:
        print("😲 Tie game !!")
    else:
        print("🐍 Python wins !!")

    while True:
        playagain = input("\nEnter Y to play again or Q to quit:\n\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return rps()
    else:
        print("\n😊 Bye !!\n")
        sys.exit()


rps()
