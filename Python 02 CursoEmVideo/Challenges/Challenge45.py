print('=====CHALLENGE 45=====')

from random import randint
from time import sleep

items = ('Rock', 'Paper', 'Scissors')
computer = randint (0,2)

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(2)

player = int(input('''Your turn to play!
[ 0 ] Rock
[ 1 ] Paper
[ 2 ] Scissors \n'''))

print('-='* 15)
print('The computer chose {}'.format(items[computer]))
print('You played {}'.format(items[player]))
print('-='* 15)

if computer == 0: #played Rock:
    if player == 0: #played Rock
        print('TIE!')
    elif player == 1: #played Paper
        print('WINNER!')
    elif player == 2: #played Scissors
        print('YOU LOSE!')

elif computer == 1: #played Paper
    if player == 0: #played Rock
        print('YOU LOSE!')
    elif player == 1: #played Paper
        print('TIE!')
    elif player == 2: #played Scissors
        print('WINNER!')

elif computer == 2: #played Scissors
    if player == 0: #played Rock
        print('WINNER!')
    elif player == 1: #played Paper
        print('YOU LOSE!')
    elif player == 2: #played Scissors
        print('TIE!')
