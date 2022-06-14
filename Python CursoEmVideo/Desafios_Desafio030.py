print('=====DESAFIO 30=====\n'
      'Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar\n')

num = int(input('Digite um número: '))
pr = num%2

if pr == 0:
    print('O número {} é par.'.format(num))

else:
    print('O número {} é impar.'.format(num))