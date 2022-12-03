print('=====CHALLENGE 56=====')

sum = 0
cont = 0
constm = 0
oldName = ''
olgAge = 0

for c in range(1, 5):
    name = input('Digite um name: ')
    age = int(input('Age: '))
    cont += 1  # this counter will be used to count the variable to average.
    sum = sum + age # sum to average the age of the group.
    sex = input('sex [M/F]: ')
    if sex in 'Mm' and age > olgAge: # check if you are a man and if your age is greater than the initial age and the others.
        olgAge = age
        oldName = name
    if sex in 'Ff' and age < 20:
        constm += 1
print(f'Average ages {sum / cont}.') # F-String print(f'{example}') replaces .format() in python3.6
print(f'The oldest man is named {oldName} and is {olgAge} years old.')
print(f'There are {constm} female(s) younger than 20.')