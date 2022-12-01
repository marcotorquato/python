print('=====CHALLENGE 39=====')

from datetime import date

year = date.today().year
born = int(input('Enter the year of your born: '))
age = year - born
lack = (18 - age)
late = (age - 18)


if age < 18:
    print('There are {} years left for you to enlist'.format(lack))
elif age == 18:
    print ('Its time for you to join the army')
else:
    print('Passed {} years the date of your enlistment!'.format(late))