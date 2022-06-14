print('=====DESAFIO 13=====')
print('\nFaça um algorítmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.')

payment = float(input('\nDigite o valor de seu salário: '))
aumento = payment + (payment * 0.15)
t_aumento = payment * 0.15

print('\nO valor atual de seu salário é de: R${:.2f} , com o aumento de 15% irá para: R${:.2f}\nO total de aumento foi de: R${:.2f}'.format(payment, aumento, t_aumento))