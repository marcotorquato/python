print('=====DESAFIO 16=====')
print('Crie um programa que leia um número real pelo teclado e mostre na sua tela a sua porção inteira')

from math import trunc

num = float(input('\nDigite um número real: '))

print('O número {} tem a parte inteira {}'.format(num, trunc(num)))