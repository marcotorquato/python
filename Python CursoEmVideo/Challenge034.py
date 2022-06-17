print('=====CHALLENGE 34=====\n'

      'Write a program that asks for an employees salary and calculates the amount of his raise\n'
      'For salary above BRL 1,250.00, calculate a 10 percent increase\n'
      'For those less than or equal, the increase is 15 percent')

salary = float(input('Enter your salary amount: '))

if salary > 1250:
    print('You will receive an increase of R${:.2f} and your total salary will be R${:.2f}'.format(salary*0.1, (salary*0.1)+salary))

else:
    print('You will receive an increase of R${:.2f} and your total salary will beR${:.2f}'.format(salary*0.15, (salary*0.15)+salary))