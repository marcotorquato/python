print('=====CHALLENGE 28=====\n'
      'Write a program that asks the user to try to find a number from 0 to 5 chosen by the computer\n'
      'The program should write to the screen if the user won or lost\n')

from random import randint
from time import sleep


al = randint(0,5)

print('\033[31m-='*58)
print('\033[36mHello, my name is R3D58 and I am in charge of thinking in numbers, can you think of the same number as me?')
print('\033[31m-=\033[m'*58)

user = int(input('\033[36mEnter a number between 0 and 5: '))

print('PROCESSING...')
sleep(2)

if user == al:
    print('You got the number right, congratulations')

elif user > 5:
    print('You chose a number greater than 5')

elif user > al:
    print('You kicked too high')

elif user < al:
    print('You kicked too low')



