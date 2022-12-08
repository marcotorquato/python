print('=====CHALLENGE 67=====')

while True:
    tab = int(input('Write a number: '))
    if tab < 0:
        break

    for c in range(1,11):
        print(f'{tab} x {c} = {tab * c}')