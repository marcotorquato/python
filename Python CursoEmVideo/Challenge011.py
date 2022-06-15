print('=====CHALLENGE 11=====')

print('\nWrite a program that reads the height and width of a wall in meters, calculates its area the amount of \paint needed to paint it, knowing that each liter of paint paints an area of ​​2m²')
width = float(input('\nDigite a largura de sua parede: '))
height = float(input('Agora digite a altura de sua parede: '))
area = width * height
paint = area / 2

print('\nYour wall area is: {}m² and the amount of paint needed will be: {}L'.format(area, paint))