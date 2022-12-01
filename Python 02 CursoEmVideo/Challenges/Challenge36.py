print('=====CHALLENGE 36=====')

houseValue= float(input('What is the value of the house? '))
salaryValue= float(input('What is the value of your salary? '))
installments= float(input('How many years do you want to pay? ')* 12)
salaryPercent = float(salaryValue * 0.3)

if houseValue/installments >= salaryPercent :
    print('Congratulations! The value of the installment does not exceed thirty percent of your salary. Your loan has been approved!')
else:
    print ('Unfortunately, the value of the installment exceeds the limit of thirty percent of your salary, you cannot finance this!')

