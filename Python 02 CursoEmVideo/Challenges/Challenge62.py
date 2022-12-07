print('=====CHALLENGE 62=====')

start = int(input('Enter the start number: '))
step = int(input('Enter the step number: '))
exit = start + (10 - 1) * step

therm = 0 
cont = 0
total = 0
more = 10
while more != 0:
    total += more
    while cont <= total:
        print('%d = ' %therm)
        therm += step
        cont += 1
    print('More')

    more = int(input('How many terms do you want to show? '))
print('END. Were shown %d terms! '%total)
