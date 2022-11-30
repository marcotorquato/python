print('=====CHALLENGE 17=====')

print('Write a program that reads the two legs of a right triangle and calculates the length of its hypotenuse')

from math import hypot

catop = float(input('Report the opposite side: '))
catadj = float(input('Now inform the adjacent side: '))

print('The triangle hypotenuse has the value of: {:.0f}'.format(hypot(catop, catadj)))

