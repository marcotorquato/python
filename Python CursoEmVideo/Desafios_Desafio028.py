print('=====DESAFIO 28=====\n'
      'Escreva um programa que peça para o usuario tentar descobrir um numero de 0 a 5 escolhido pelo computador\n'
      'O programa deverá escrever na tela se o usuário venceu ou perdeu\n')

from random import randint
from time import sleep


al = randint(0,5)

print('\033[31m-='*58)
print('\033[36mOlá, meu nome é R3D58 e sou encarregado de pensar em números, será que você consegue pensar no mesmo número que eu?')
print('\033[31m-=\033[m'*58)

usuario = int(input('\033[36mDigite um número entre 0 e 5: '))

print('PROCESSANDO...')
sleep(2)

if usuario == al:
    print('Você acertou o número, parabéns')

elif usuario > 5:
    print('Você escolheu um número maior que 5')

elif usuario > al:
    print('Você chutou alto demais')

elif usuario < al:
    print('Você chutou baixo demais')



