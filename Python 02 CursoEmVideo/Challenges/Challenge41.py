print('=====CHALLENGE 41=====')

from datetime import date

year = date.today().year


born = int(input('What year were you born? '))
now = (year - born)

if year <= 9:
    print ('Category Little')
elif year <= 14:
    print ('Category Children')
elif year <= 19:
    print ('Category Jr')
elif year <= 20:
    print ('Category Senior')
else :
    print ('Category Master')