print('=====CHALLENGE 33=====\n'

      'Write a program that reads three numbers and shows which is the largest and which is the smallest.')

n1 = int(input('Enter a number: '))
n2 = int(input('Now report another: '))
n3 = int(input('And now one more: '))

if n1 > n2 and n1 > n3:
    print('The number {} is bigger than the others'.format(n1))
    if n2 > n3:
        print('The number {} is the smallest of all'.format(n3))
    else:
        print('The number {} is the smallest of all'.format(n2))

elif n2 > n1 and n2 > n3:
    print('The number {} is bigger than the others'.format(n2))
    if n1 > n3:
        print('The number {} is the smallest of all'.format(n3))
    else:
        print('The number {} is the smallest of all'.format(n1))

elif n3 > n1 and n3 > n2:
    print('The number {} is bigger than the others'.format(n3))
    if n1 > n2:
        print('The number {} is the smallest of all'.format(n2))
    else:
        print('The number {} is the smallest of all'.format(n1))