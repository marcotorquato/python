print('=====CHALLENGE 23=====')

print('Write a program that reads a number from 0 to 9999 and displays each of the separate digits on the screen.')

num = str(input('Enter a number from 0 to 9999: ')).zfill(4)

print('\nThe number entered was: {}'.format(num))
print('Your unit is: {}'.format(num[3]))
print('Your ten is: {}'.format(num[2]))
print('Your hundred is: {}'.format(num[1]))
print('Your thousand is: {}'.format(num[0]))