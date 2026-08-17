# imports
import sys
import random
from enum import Enum


def play_rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def game_rps():
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input("Enter...\n1 for Rock,\n2 for Paper, \n3 for Scissors:")

        player = int(playerchoice)

        if playerchoice not in ["1", "2", "3"]:
            print("Please enter number between 1 to 3.")
            return game_rps()
        computerchoice = random.choice("123")
        computer = int(computerchoice)
        print("You chose: " + str(RPS(player)).replace("RPS.", ""))
        print("Computer chose: " + str(RPS(computer)).replace("RPS.", ""))
        print("")

        def decide_winner():
            nonlocal player_wins
            nonlocal python_wins

            if (
                (player == 1 and computer == 3)
                or (player == 2 and computer == 1)
                or (player == 3 and computer == 2)
            ):
                player_wins += 1
                return "🍕 You win !!\n"
            elif player == computer:
                return "😲 Tie game !!\n"
            else:
                python_wins += 1
                return "🐍Python wins !!"

        game_result = decide_winner()

        print(game_result)

        nonlocal game_count
        game_count += 1

        print("You win: " + str(player_wins))
        print("Computer win: " + str(python_wins))
        print("Games: " + str(game_count))

        while True:
            playagain = input("Enter Y for Yes or Q for Quit:")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            return game_rps()
        else:
            print("👌 Bye !!")
            sys.exit()

    return game_rps


play = play_rps()
play()
