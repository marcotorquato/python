print('=====CHALLENGE 64=====')
num = 0
count = 0
sum = 0
num = int(input('[999 to STOP] or Write a number: '))

while num != 999:
  count +=1
  sum += num
  num = int(input('[999 to STOP] or Write a number: '))

print('Were entered %d numbers and their sum is: %d'%(count,sum))


