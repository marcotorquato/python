print('=====CHALLENGE 63=====')

ant, pos = 1, 0
num = int(input('How many terms of the Fibonacci sequence do you want: '))
print(0, end=' ')
for c in range(1, num):
    prox = pos + ant
    ant = pos
    pos = prox
    print(prox, end=' ')
