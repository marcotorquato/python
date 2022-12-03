for c in range (0,6):
    print('Hi')
print('END')

print('-='*30)

i = int(input('Start '))
e = int(input('END '))
s = int(input('Step '))

# the last condition of the range that will determine the steps (what it will do). this example S
for c in range(i, e+1, s):
    print(c)
print('END')

print('-='*30)

s = 0 
for c in range (0,4):
    n = int(input('Write a value: '))
    s += n
print ('The sum of the values ​​are: %s'%s)