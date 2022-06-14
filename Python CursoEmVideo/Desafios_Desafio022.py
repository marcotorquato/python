print(' '*39+'=====DESAFIO 22=====')
print("""Crie um programa que leia o nome completo de uma pessoa e mostre: 
o nome com todas as letras maiusculas e minusculas, quantas lentras tem ao todo(sem considerar espaços)
e quantas letras tem o primeiro nome""")

nome = str(input("\nDigite seu nome e sobrenome: ")).strip()
dividido = nome.split()
print('\nO seu nome com todas as letras maiusculas ficará: {}'.format(nome.upper()))
print('\nEm minusculas: {}'.format(nome.lower()))
print('\nA quantidade de letras é: {}'.format(len(nome) - nome.count(' ')))
print('\nE a quantidade de letras do seu primeiro nome é de: {}'.format(len(dividido[0])))