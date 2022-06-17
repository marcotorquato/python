print('=====CHALLENGE 32=====\n'
      
      'Make a program that reads any year and shows if it is Leap\n')

from datetime import date

year = int(input('Tell the year? Put 0 to analyze the current year: '))

if year == 0:
    year = date.today().year

if year % 400 == 0:
    print('The year {} is a leap year'.format(year))

elif year % 100 == 0:
    print('The year {} is not a leap year'.format(year))

elif year % 4 == 0:
    print('The year {} is a leap year'.format(year))

else:
    print('The year {} is not a leap year'.format(year))
