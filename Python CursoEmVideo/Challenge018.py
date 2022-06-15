print('=====CHALLENGE 17=====')

print('Write a program that reads any angle and displays the value of its sine, cosine and tangent on the screen.')

from math import sin, cos, tan, radians

ang = float(input('Enter the value of an angle: '))
sine = sin(radians(ang))
cos = cos(radians(ang))
tang = tan(radians(ang))
print("Your sine: {:.2f}"
      "\nYour cosine: {:.2f}"
      "\nYour tangent: {:.2f}".format(sine, cos, tang))