print('=====CHALLENGE 68=====')
from random import randint

loser = winner = 0

while loser == 0:

    number = int(input('Write a number: '))
    option = str(input('Choose Even or Odd ')).upper()

    npc = randint(0,10)
    sum = number + npc

    if option == 'EVEN' and sum % 2 == 0:
            print(f'''\033[1;30mO jogador jogou: {number}\033[m 
    \033[1;31mThe NPC played: {npc}\033[m 
    \033[1;32msum of numbers: {sum}\033[m
    \033[1;33mResult: EVEN\033[m 
    \033[1;34mYou won !\033[m ''')
            winner += 1

    elif option == 'EVEN' and sum % 2 == 1:
        print(f'''\033[1;30mO jogador jogou: {number}\033[m 
    \033[1;31mThe NPC played: {npc}\033[m 
    \033[1;32mSum of numbers: {sum}\033[m
    \033[1;33mResult: ODD\033[m 
    \033[1;34mYou lost !\033[m ''')
        loser = 1

    elif option == 'ODD' and sum % 2 == 0:
        print(f'''\033[1;30mO jogador jogou: {number}\033[m 
    \033[1;31mThe NPC played: {npc}\033[m 
    \033[1;32msum of numbers: {sum}\033[m
    \033[1;33mResult: EVEN\033[m 
    \033[1;34mYou lost !\033[m ''')
        loser = 1

    elif option == 'ODD' and sum % 2 == 1:
        print(f'''\033[1;30mO jogador jogou: {number}\033[m 
    \033[1;31mThe NPC played: {npc}\033[m 
    \033[1;32msum of numbers: {sum}\033[m
    \033[1;33mResult: ODD\033[m 
    \033[1;34mYou won !\033[m ''')
        winner += 1

print(f'You won {winner} times')