print('=====CHALLENGE 56=====')

sumAge = 0
media = 0
largerAgeMan = 0 
oldName = ''
underWoman20 = 0

for p in range(1, 5):
    print('------- %d PERSON -------' %(p))
    name = str(input('Name: ')).strip()    
    age = int(input('Age: '))
    sex = str(input('Sex [M/F]: ')).strip()
    sumAge += age
    if p == 1 and sex in 'Mm':
        oldNameman = age
        oldName = name
    if sex in 'Mm' and age > largerAgeMan:
        largerAgeMan = age  
        oldName = name
    if sex in 'Ff' and age < 20:
        underWoman20 += 1
media = sumAge / 4

print('The media of group is %d'%(media))
print('The older man has {} and is called {}' .format(largerAgeMan, oldName))
print('Are %d women under 20 years old' %(underWoman20))