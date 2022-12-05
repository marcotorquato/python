print('=====CHALLENGE 51=====')


start = int(input('Enter the reason for the P.A.: '))
step = int(input('Enter the reason for the P.A.: '))
exit = start + (10 - 1) * step

for c in range(start, exit + 1, step):
    print('-> {}'.format(c))