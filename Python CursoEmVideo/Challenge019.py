print('=====CHALLENGE 19=====')

print('A teacher who draws one of his four students to erase the board. Make a program that helps him, reading\their name and writing the name of the chosen one')

from random import choice

a1 = input('First student name: ')
a2 = input('Second students name: ')
a3 = input('Third students name: ')
a4 = input('Fourth student name: ')

print('\nThe chosen student was:{}'.format(choice([a1, a2, a3, a4])))