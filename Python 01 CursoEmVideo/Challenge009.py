print('=====CHALLENGE 09=====')

print('\nWrite a program that reads an integer and displays its multiplication table.')
num = int(input('Enter a number:'))
counter = 0
tab = 10
while counter <= tab:
    res = num * counter 
    # outside the loop the account doesn't work
    print('{} * {} = {}'.format(num, counter, res))
    counter += 1
