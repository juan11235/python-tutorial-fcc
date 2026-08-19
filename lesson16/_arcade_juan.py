import sys
import _rps_juan
import _guess_number

def arcade_game(name='Player One'):
    welcome_back = False
    while True:
        if welcome_back == True:
            print(f'Hi {name}, welcome back to the arcade !!')
        playerchoice = input(f'Please enter 1 to play rps, 2 to play guess_number or x to quit arcade')
        if playerchoice not in ['1', '2', 'x']:
            print(f'{name}, please enter 1, 2 or x:')
            return arcade_game()
        welcome_back = True
        if playerchoice == '1':
            rps_arcade = _rps_juan(name)
            rps_arcade()
        elif playerchoice == '2':
            guess_number_arcade = _guess_number(name)
            guess_number_arcade()
        else:
            if __name__ == '__main__':
                print(f'Bye {name}')
                sys.exit
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Provides a more personalized experience')
    parser.add_argument('-n', 'name', metavar='name', required=True, help='The name of the person playing the game')
    args = parser.parse_args()
    print(f'Hi {args.name}, welcome to the arcade !!')
    arcade_game(args.name)