print('=====CHALLENGE 50=====')

sum = 0
for c in range (0, 6):
    num = int(input('Write a number: '))
    if num % 2 == 0:
        sum += num
print(sum)