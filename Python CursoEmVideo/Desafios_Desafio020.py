print('=====DESAFIO 20=====')
print('O mesmo professor quer sortear a orde de apresentação de trabalho dos alunos, faça um programa que mostre o nome dos\nquatro alunos e mostre a ordem sorteada.')

from random import sample, choice

a1 = input('\nNome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do terceiro aluno: ')
a4 = input('Nome do quarto aluno: ')



print('A ordem de apresentação é de: {}'.format(sample((a1, a2, a3, a4),k=4)))
