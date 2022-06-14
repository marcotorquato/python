from random import randint

print('Welcome!\n')
prizedraw = randint (1,15)
random = 0
while random != prizedraw:
    random = int(input('Random Number '))
    if random == prizedraw:
        print('Winner!\n')
    if random > prizedraw:
        print('smaller    \n')
    if random < prizedraw:
        print('larger\n')
print(('End Game!'))