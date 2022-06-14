print('=====DESAFIO 09=====')
print('\nFaça um programa que leia um número inteiro e mostre a sua tabuada.')
num = int(input('Digite um número:'))
counter = 0
tab = 10
while counter <= tab:
    res = num * counter #estando fora do loop a conta não funciona
    print('{} * {} = {}'.format(num, counter, res))
    counter += 1
