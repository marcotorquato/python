print('Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separademente')

nome = str(input('\nDigite o seu nome: ')).strip().lower().title().split()

print('\nPrimeiro nome: {}'.format(nome[0]))
print('Segundo nome: {}'.format(nome[len(nome)-1]))