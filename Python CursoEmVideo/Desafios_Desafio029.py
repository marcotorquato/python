print('=====DESAFIO 29=====\n'
      'Escreva um programa que leia a velocidade de um carro\n'
      'Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado\n'
      'A multa vai custar R$7,00 por cada Km acima do limite.\n')

vel = int(input('Informe a velocidade do carro: '))

if vel > 80:
    print('Você foi multado em: R${:.2f}'.format((vel - 80)*7))
else:
    print('Continue dirigindo com cuidado, tenha um bom dia! :)')