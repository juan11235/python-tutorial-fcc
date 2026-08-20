import sys
import random
from enum import Enum


def rps(name="Player one"):
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def rps_play():
        nonlocal game_count, player_wins, computer_wins, name

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(f"Please enter 1 for Rock, 2 for Paper or 3 for Scissors:")
        if playerchoice.lower() not in ["1", "2", "3"]:
            print(f"{name}, please enter a number between 1 to 3:")
            return rps_play()
        computerchoice = random.choice("123")

        player = int(playerchoice)
        computer = int(computerchoice)
        print(f"{name}, you chose: {RPS(player).name}")
        print(f"Computer chose: {RPS(computer).name}")

        def decide_winner(player, computer):
            nonlocal name, player_wins, computer_wins
            if (
                (player == 1 and computer == 3)
                or (player == 2 and computer == 1)
                or (player == 3 and computer == 2)
            ):
                player_wins += 1
                return f"{name} you won !!"
            elif player == computer:
                return f"Tie game !!"
            else:
                computer_wins += 1
                return f"Computer won !!"

        game_result = decide_winner(player, computer)
        print(game_result)
        game_count += 1
        print(f"Game count: {game_count}")
        print(f"{name} wins: {player_wins}")
        print(f"Computer wins: {computer_wins}")
        while True:
            playagain = input(f"Enter Y to play again or Q to quit: ")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            return rps_play()
        else:
            if __name__ == "__main__":
                print(f"Bye {name} !!")
                sys.exit()
            else:
                return

    return rps_play


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a more personalized experience"
    )
    parser.add_argument(
        "-n", "-name", metavar="name", help="The name of the player", required=True
    )
    args = parser.parse_args()
    play_this = rps(args.name)
    play_this()
