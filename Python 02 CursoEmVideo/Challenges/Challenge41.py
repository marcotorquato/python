print('=====CHALLENGE 40=====')

age = int(input('How old are you? '))

if age <= 9:
    print ('Category Little')
elif age <= 14:
    print ('Category Children')
elif age <= 19:
    print ('Category Jr')
elif age <= 20:
    print ('Category Senior')
else :
    print ('Category Master')