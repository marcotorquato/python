print('=====DESAFIO 35=====\n'
      'Desenvolva um programa que leia o comprimento de três retas e diga se elas podem ou não formar um triângulo')

a = float(input('Informe o comprimento da primeira reta: '))
b = float(input('Da segunda reta: '))
c = float(input('Da terceira reta: '))

if b-c < a < b+c and a-c < b < a+c and a-b < c < a+b:
    print('É possivel fazer um triangulo com essas retas.')
else:
    print('Não é possível fazer um triangulo com essas retas.')
