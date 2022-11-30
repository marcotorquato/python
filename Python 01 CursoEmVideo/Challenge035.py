print('=====CHALLENGE 35=====\n'

      'Develop a program that reads the length of three lines and tells whether or not they can form a triangle')

a = float(input('Enter the length of the first straight line: '))
b = float(input('From the second line: '))
c = float(input('From the third line: '))

if b-c < a < b+c and a-c < b < a+c and a-b < c < a+b:
    print('It is possible to make a triangle with these lines.')
else:
    print('Cannot make a triangle with these lines.')
