import sys
import random
from enum import Enum


def rps_game(name="Player One"):
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play():
        nonlocal name, player_wins, computer_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            f"{name} please enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n"
        )
        player = int(playerchoice)
        if player not in [1, 2, 3]:
            print(f"{name} please enter number between 1 to 3:")
            return play()
        computerchoice = random.choice("123")
        computer = int(computerchoice)
        print(f'{name} you chose {str(RPS(player)).replace("RPS.", "").title()}.')
        print(f'Computer chose {str(RPS(computer)).replace("RPS.", "").title()}.')

        def decide_winner(player, computer):
            nonlocal player_wins, computer_wins, name
            if (
                (player == 1 and computer == 3)
                or (player == 2 and computer == 1)
                or (player == 3 and computer == 2)
            ):
                player_wins += 1
                return f"{name} you win !!"
            elif player == computer:
                return "Tie game !!"
            else:
                computer_wins += 1
                return f"Computer wins !!"

        winner = decide_winner(player, computer)
        print(winner)
        nonlocal game_count
        game_count += 1
        print(f"{name} wins: {player_wins}")
        print(f"Computer wins: {computer_wins}")
        print(f"Game Count: {game_count}")
        while True:
            playagain = input(
                f"{name} do you want to play again ?\nIf yes press Y or Q to quit:"
            )
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            return play()
        else:
            print(f"Bye {name} !")
            sys.exit()

    return play


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a more personalized experience."
    )
    parser.add_argument("-n", "--name", required=True, help="Name of player")
    args = parser.parse_args()
    rock_paper_scissors = rps_game(args.name)
    rock_paper_scissors()
