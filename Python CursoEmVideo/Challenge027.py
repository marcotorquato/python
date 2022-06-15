print('=====CHALLENGE 27=====')

print('Write a program that reads a persons full name, then displays the first and last names separately')

name = str(input('\nEnter your name: ')).strip().lower().title().split()

print('\nFirst name: {}'.format(name[0]))
print('Second name: {}'.format(name[len(name)-1]))