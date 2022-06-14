print('=====DESAFIO 33=====\n'
      'Faça um programa que leia três números e mostre qual é o maior e qual é o menor')

n1 = int(input('Informe um número: '))
n2 = int(input('Agora informe outro: '))
n3 = int(input('E agora mais um: '))

if n1 > n2 and n1 > n3:
    print('O número {} é maior que os outros'.format(n1))
    if n2 > n3:
        print('O número {} é o menor de todos'.format(n3))
    else:
        print('O número {} é o menor de todos'.format(n2))

elif n2 > n1 and n2 > n3:
    print('O número {} é maior que os outros'.format(n2))
    if n1 > n3:
        print('O número {} é o menor de todos'.format(n3))
    else:
        print('O número {} é o menor de todos'.format(n1))

elif n3 > n1 and n3 > n2:
    print('O número {} é maior que os outros'.format(n3))
    if n1 > n2:
        print('O número {} é o menor de todos'.format(n2))
    else:
        print('O número {} é o menor de todos'.format(n1))