print('=====DESAFIO 31=====\n'
      'Desenvolva um programa que pergunte a distancia de uma viagem em km.\n'
      'Calcule o preço de uma passagem, cobrando R$0,50 por KM para viagens de até 200km\n'
      'E R$0,45 para viagens mais longes\n')

viagem = int(input('Informe a distância em Kilômetros da viagem: '))

above = 0.45
eq_o_un = 0.50

if viagem <= 200:
    print('O valor da viagem ficou em: R${:.2f}'.format((eq_o_un*viagem)))
else:
    print('O valor da viagem ficou em: R${:.2f}'.format(above*viagem))
