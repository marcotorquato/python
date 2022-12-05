print('=====CHALLENGE 58=====')

from random import randint

print('Welcome!\n')
prizedraw = randint (1,10)
random = 0
error = 1
while random != prizedraw:
    random = int(input('Random Number '))
    if random == prizedraw:
        print('Winner!\n')
    if random > prizedraw:
        error += 1
        print('smaller    \n')
    if random < prizedraw:
        error += 1
        print('larger\n')
print(('End Game! You needed {} chances to get it right!'.format(error)))