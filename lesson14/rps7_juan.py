import sys
import random
from enum import Enum


def play_the_game():
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def rps():
        nonlocal player_wins
        nonlocal computer_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input("Enter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:")
        player = int(playerchoice)
        if playerchoice not in ["1", "2", "3"]:
            return rps()
        computerchoice = random.choice("123")
        computer = int(computerchoice)
        print(f"You chose: {str(RPS(player)).replace('RPS.', '').title()}")
        print(f"Computer chose: {str(RPS(computer)).replace('RPS.', '').title()}")

        def decide_winner():
            nonlocal player_wins
            nonlocal computer_wins
            if (
                (player == 1 and computer == 3)
                or (player == 2 and computer == 1)
                or (player == 3 and computer == 2)
            ):
                player_wins += 1
                return "You win"
            elif player == computer:
                return "Tie game"
            else:
                computer_wins += 1
                return "Computer wins"

        winner = decide_winner()
        print(winner)
        nonlocal game_count
        game_count += 1
        print(f"You win: {player_wins}")
        print(f"Computer wins: {computer_wins}")
        print(f"Game count: {game_count}")
        while True:
            playagain = input("Enter Y for Yes or Q for Quit:")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            rps()
        else:
            print("Bye")
            sys.exit()

    return rps()


play = play_the_game
if __name__ == "__main__":
    play()
