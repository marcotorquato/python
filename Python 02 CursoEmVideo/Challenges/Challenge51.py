print('=====CHALLENGE 51=====')


thirt = int(input('Enter the reason for the P.A.: '))
sec = int(input('Enter the reason for the P.A.: '))
ene = thirt + (10 - 1) * sec

for c in range(thirt, ene + 1, sec):
    print('=> {}'.format(c))