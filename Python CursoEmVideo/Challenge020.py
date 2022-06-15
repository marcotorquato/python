print('=====CHALLENGE 20=====')
print('The same teacher wants to draw the order of presentation of the students work, make a program that shows the names of the\n four students and shows the order drawn.')

from random import sample, choice

a1 = input('First student name: ')
a2 = input('Second students name: ')
a3 = input('Third students name: ')
a4 = input('Fourth student name: ')



print('The order of presentation is: {}'.format(sample((a1, a2, a3, a4),k=4)))
