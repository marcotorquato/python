print('=====CHALLENGE 42=====')

a = float(input('Enter the length of the first straight line: '))
b = float(input('From the second line: '))
c = float(input('From the third line: '))

if b-c < a < b+c and a-c < b < a+c and a-b < c < a+b:
    print('It is possible to make a triangle with these lines.', end='')
    if a == b == c:
        print('EQUILATERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('Cannot make a triangle with these lines.')
