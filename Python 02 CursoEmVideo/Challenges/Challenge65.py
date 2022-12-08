print('=====CHALLENGE 65=====')

answer = 'S'
sum = amount = media = 0

while answer in 'Ss':
    num = int(input('Write a number: '))
    sum += num
    amount += 1
    if amount == 1:
        larger = smaller = num 
    else:
        if num > larger:
            larger = num
        if num < smaller:
            smaller = num

    answer = str(input('Continue? [S/N] ')).upper().strip()[0]

media = (sum/amount)
print('You typed %d numbers and the average is: %d.'%(amount,media))
print('The largest value entered was %d and the smallest was %d'%(larger,smaller))
