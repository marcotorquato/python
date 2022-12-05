print('=====CHALLENGE 51=====')


start = int(input('Enter the start number: '))
step = int(input('Enter the step number: '))
exit = start + (10 - 1) * step

for c in range(start, exit + 1, step):
    print('-> {}'.format(c))