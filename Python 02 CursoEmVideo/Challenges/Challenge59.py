print('=====CHALLENGE 59=====')
from time import sleep 

a = int(input('Write a number: '))
b = int(input('Write a number: '))
option = int(input('''[1] Sum
    [2] Multiply
    [3] Bigger
    [4] Insert new numbers
    [5] Exit the program.
    What is your option?\n'''
    ''))

while option.upper != 5 and option in 'SN':
    if option == 1 :
        print(f'The sum of {a} + {b} is: {a+b}')
    elif option == 2:
        print(f'The multiplication of {a} * {b} is: {a*b}')
    elif option == 3:
        if a > b:
            print(f'The first number is {a} and is greater than the second number {b}')
        elif a < b:
            print(f'The second number is {b} and is greater than the first {a}')
        else:
            print('The numbers are the same')
    elif option == 4:
        a = int(input('Write a number: '))
        b = int(input('Write a number: '))
    elif option == 5:
        break
    else:
        print('No option! Type again.')
        print('-=' * 50)
        sleep(1.0)
print('You left the program! Until later!')
