import sys
import random
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    computer_wins = 0

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    def play_rps():
        nonlocal player_wins
        nonlocal computer_wins
        playerchoice = input("Enter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n")
        player = int(playerchoice)
        if playerchoice not in ["1", "2", "3"]:
            return play_rps()
        computerchoice = random.choice("123")
        computer = int(computerchoice)
        print(f"you chose {str(RPS(player)).replace('RPS.', '').title()}")
        print(f"computer chose {str(RPS(computer)).replace('RPS.', '').title()}")

        def decide_winner():
            nonlocal player_wins
            nonlocal computer_wins
            if (
                (player == 1 and computer == 3)
                or (player == 2 and computer == 1)
                or (player == 3 and computer == 2)
            ):
                player_wins += 1
                return "player wins"
            elif player == computer:
                return "Tie game"
            else:
                computer_wins += 1
                return "Computer wins"

        game_result = decide_winner()
        print(game_result)
        nonlocal game_count
        game_count += 1
        print(f"You win: {str(player_wins)}")
        print(f"Computer win: {str(computer_wins)}")
        print(f"Game count: {str(game_count)}")
        while True:
            playagain = input("Enter y for Yes or Q for Quit:")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            return play_rps()
        else:
            print("Bye")
            sys.exit()

    return play_rps


play = rps()
play()
