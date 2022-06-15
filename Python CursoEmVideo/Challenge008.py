print('=====CHALLENGE 08=====')

print('\nWrite a program that reads a value in meters and displays it converted to all measurements.')
num = float(input('Enter the value of the footage:'))
dm = num * 10
cm = num * 100
mm = num * 1000
dec = num / 10
hm = num / 100 
km = num / 1000
print('\nThe value: {}m \nor millimeter: {:.0f}mm\nor centimeter: {:.0f}cm\nor decimeter: {:.0f}dm \nor decameter: {}dam\nor hectometer: {}hm \n and in kilometer: {}km'.format(num, mm, cm, dm, dec, hm, km))
