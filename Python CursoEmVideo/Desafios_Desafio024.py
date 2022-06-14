print('=====DESAFIO 24=====')
print('Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com santo')

cidade = str(input('Digite o nome de sua cidade: ')).strip().lower().capitalize()

print('Santo' in cidade[:5])