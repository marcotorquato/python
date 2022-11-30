print('=====CHALLENGE 16=====')

print('Create a program that reads a real number from the keyboard and displays its entire portion on your screen')

from math import trunc

num = float(input('\nEnter a real number: '))

print('The number {} has the integer part {}'.format(num, trunc(num)))