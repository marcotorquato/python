print('=====CHALLENGE 13=====')

print('\nRun an algorithm that reads an employees salary and displays their new salary with a 15 percent increase.')

payment = float(input('\nEnter your salary amount: '))
increase = payment + (payment * 0.15)
t_increase = payment * 0.15

print('\nThe current salary is: R${:.2f} , with a 15 percent increase it will go to: R${:.2f}\nThe total increase was: R${:.2f}'.format(payment, increase, t_increase))