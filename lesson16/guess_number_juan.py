import random
import sys

def game(name='Player One'):
    game_count = 0
    player_wins = 0

    def juego_logica():
        nonlocal name
        nonlocal player_wins

        player_choice = input(f'{name}, guess a number between 1 to 3:')
        if player_choice not in ['1', '2', '3']:
            print(f'{name}, please enter a number between 1 and 3:')
            return juego_logica()

        computer_choice = random.choice('123')

        print(f'{name} you chose {player_choice}')
        print(f'Computer chose {computer_choice}')
        
        player = int(player_choice)
        computer = int(computer_choice)

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f'{name}, you won !'
            else:
                return f'Computer wins !'

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f'Game count: {game_count}')
        print(f'{name} wins: {player_wins}')
        print(f'Porcentaje ganado: {player_wins/game_count:.2%}')

        print('Play again?')
        while True:
            playagain = input(f'{name}, press Y to play again or Q to quit:')
            if playagain.lower() not in ['y', 'q']:
                continue
            else:
                break
        if playagain.lower() == 'y':
            return juego_logica()
        else:
            print(f'Bye {name}')
            if __name__ == '__main__':
                sys.exit('Bye bye')
            else:
                return
    return juego_logica
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )
    
    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True, help='The name of the person playing the game.'
    )

    args = parser.parse_args()
    guess_my_number = game(args.name)
    guess_my_number()