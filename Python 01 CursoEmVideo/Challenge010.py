print('=====CHALLENGE 10=====')

print('\nCreate a program that reads how much money a person has and displays the dollar amount.')
num = float(input('Enter the amount in Reais available:'))
res = num / 5.11
print('\nYou have R${} and in dollars you have US${:.2f}'.format(num, res))