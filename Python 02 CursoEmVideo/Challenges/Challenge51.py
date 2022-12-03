print('=====CHALLENGE 51=====')


start = int(input('Enter the reason for the P.A.: '))
step = int(input('Enter the reason for the P.A.: '))
end = start + (10 - 1) * step

for c in range(start, end + 1, step):
    print('-> {}'.format(c))