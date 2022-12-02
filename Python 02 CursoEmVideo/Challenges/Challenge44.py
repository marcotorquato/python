print('=====CHALLENGE 44=====')

value = float(input('What is the purchase price? '))
payFor = float(input('''What is the payment method?
[ 1 ] CASH 
[ 2 ] 1x ON CARD
[ 3 ] 2x ON THE CARD
[ 4 ] MORE THAN 3x ON THE CARD\n '''))

if payFor == 1:
    sale10 = value - (value * 10 / 100)
    print('You will pay in CASH! the value will be: $%.2f'%inCash10)
elif payFor == 2:
    sale5 = value - (value * 5 / 100 )
    print ('You will pay in 1x ON CARD! the value will be: $%.2f'%inCash5)
elif payFor == 3:
    print ('You will pay in 2x ON THE CARD! the value will be: $%.2f'%value)
elif payFor == 4:
    more3 = value + (value * 20 / 100)
    installments = int(input('Number of installments? '))
    par = more3 / installments
    print ('You will pay in MORE THAN 3x ON THE CARD! the value will be: ${:.2}!\n Will be {} installments of ${:.2f}!' .format(more3, installments, par))
else:
    print('INVALID')