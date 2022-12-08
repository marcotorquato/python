print('=====CHALLENGE 70=====')

cheap = ''
total = over1k = count = under = 0
result = ''
while result != 'N':
    name = input('Enter the name of the product: ')
    value = float(input('Enter the price of the product $  '))
    count += 1
    result = input('Wishes to continue ? [S/N] ').upper()[0].strip()

    if value > 1000:
        over1k += 1

    if count == 1:
        under = value
    else:
        if value < under:
            under = value
            cheap = name

    total = total + value

    while result not in 'SNsn':
        result = input('Incorrect answer. Type again [S/N]: ').upper()[0].strip()

print('{:-^60}'.format('End of the program'))

print(f'total spent: {total}')
print(f'Products that cost more than $1000: {over1k} ')
print(f'The product is cheaper: {cheap} with a price of ${under}')