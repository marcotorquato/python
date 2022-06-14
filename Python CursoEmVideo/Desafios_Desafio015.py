print('=====DESAFIO 015=====')
print("Escreva um programa que pergunta a quantidade de KM percorridos por um carro alugado e a quantidade de dias "
      "pelos\nquais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,"
      "15 por Km rodado.")

dias = int(input('\nQuantidade de dias alugado: '))* 60
km = int(input('Quantidade de Km rodados: '))* 0.15

print('O total a ser pago é de: R${:.2f}'.format(dias + km))
