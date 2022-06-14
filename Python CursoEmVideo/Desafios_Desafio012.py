print('=====DESAFIO 12=====')
print('\nFaça um algoritmo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto')

produto = float(input('Digite o valor do produto: '))
desc = produto - (produto * 0.05)
vdesc = produto * 0.05


print('O valor do produto com desconto de 5% é de: R${:.2f}'.format(desc))
print('O preço abatido do produto foi de: R${:.2f}'.format(vdesc))


#melhorar o código para ler o preço de vários produtos e mostrar o preço abatido de cada um ao final da operação