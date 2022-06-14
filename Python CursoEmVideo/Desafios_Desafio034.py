print('=====DESAFIO 34=====\n'
      'Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento\n'
      'Para salário superiores a R$1.250,00, calcule um aumento de 10%\n'
      'Para os inferiores ou iguais o aumento é de 15%')

salario = float(input('Informe o valor do seu salário: '))

if salario > 1250:
    print('Você receberá um aumento no valor de R${:.2f} e seu salário total será de R${:.2f}'.format(salario*0.1, (salario*0.1)+salario))

else:
    print('Você receberá um aumento no valor de R${:.2f} e seu salário total será de R${:.2f}'.format(salario*0.15, (salario*0.15)+salario))