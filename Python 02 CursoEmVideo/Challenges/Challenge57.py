print('=====CHALLENGE 57=====')


sex = input('Write a SEX [M/F]: ').strip().upper()

while sex not in 'MF':
    sex = input('Type again, just [M/F]:').strip().upper()
print('Nice')