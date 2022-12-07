print('=====CHALLENGE 61=====')


start = int(input('Enter the start number: '))
step = int(input('Enter the step number: '))
exit = start + (10 - 1) * step

therm = 1
cont = 0
while cont <= 10:
    print('%d = ' %therm)
    therm += step
    cont += 1
print('END')

