print('=====CHALLENGE 39=====')

from datetime import date


born = float(input('Enter the year of your birth'))
lack = 18 - born
late = born - 18



if date.year - born < 18:
    print('There are {lack} years left for you to enlist')
elif date.year - born == 18:
    print ('Its time for you to join the army')
else:
    print('Passed {late} the date of your enlistment!')