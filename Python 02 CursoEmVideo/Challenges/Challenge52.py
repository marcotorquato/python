print('=====CHALLENGE 52=====')

num = int(input('Write a number: '))
cont = 0

for c in range(1, num + 1):
    cousin = num % c == 0

    if cousin is True:
        cont = cont + 1
if cont == 2:
    print('{} is a cousin number.'.format(num))
else:
    print ('{} its not a cousin number.'.format(num))