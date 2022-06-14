print('=====DESAFIO 11=====')
print('\nFaça um programa que leia a altura e largura de uma parede em metros, calcule sua área a quantidade necessária de \ntinta para pintá-la, sabendo qeu cada litro de tinta pinta uma área de 2m²')
larg = float(input('\nDigite a largura de sua parede: '))
alt = float(input('Agora digite a altura de sua parede: '))
area = larg * alt
tinta = area / 2

print('\nA área de sua parede é de: {}m² e a quantidade de tinta necessária será: {}L'.format(area, tinta))