print('=====CHALLENGE 54=====')

from datetime import date

smaller = 0
larger = 0
today = date.today().year


for c in range(0, 7):
    date = int(input('Type a date born: '))
    if today - date < 21:
        smaller += 1
    elif today - date >= 21:
        larger += 1
print('{} is smaller.'.format(smaller))
print('{} are larger.'.format(larger))