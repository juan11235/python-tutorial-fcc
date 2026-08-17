import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")

playerchoice = input("Enter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n")
print("")
player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must choose between 1 and 3.\n")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("You chose: " + str(RPS(player)).replace("RPS.", ""))
print("Computer chose: " + str(RPS(computer)).replace("RPS.", "") + "\n")

if player == 1 and computer == 3:
    print("🍕You win!")
elif player == 2 and computer == 1:
    print("🍕You win!")
elif player == 3 and computer == 2:
    print("🍕You win!")
elif player == computer:
    print("😲Tie game!")
else:
    print("🐍Python wins!")
print("")
