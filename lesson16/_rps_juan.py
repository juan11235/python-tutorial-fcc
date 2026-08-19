import sys
import random
from enum import Enum

def rps(name='Player one'):
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def rps_play():
        nonlocal game_count, player_wins, computer_wins, name

        class RPS(Enum):
                ROCK = 1
                PAPER = 2
                SCISSORS = 3
        playerchoice = input(f'Please enter 1 for Rock, 2 for Paper or 3 for Scissors:')
        if playerchoice.lower() not in ['1', '2', '3']:
             print(f'{name}, please enter a number between 1 to 3:')
             return rps_play()
        computerchoice = random.choice('123')
        player = int(playerchoice)
        computer = int(computerchoice)
        