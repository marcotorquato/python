print('=====CHALLENGE 30=====\n'


      'Create a program that reads an integer and shows on the screen if it is even or odd\n')

num = int(input('Enter a number: '))
even = num%2

if even == 0:
    print('The number {} is even.'.format(num))

else:
    print('The number {} is odd.'.format(num))