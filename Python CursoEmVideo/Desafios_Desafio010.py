print('=====DESAFIO 10=====')
print('\nCrie um programa que lea quanto dinheiro uma pessoa tem e mostre a quantidade em dolar.')
num = float(input('Digite o valor em real disponivel:'))
res = num / 3.27
print('\nVocê possui R${} e em dólares você tem US${:.2f}'.format(num, res))