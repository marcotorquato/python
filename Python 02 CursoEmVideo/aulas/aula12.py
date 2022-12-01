name = str (input('What is your name?'))
if name == 'Marco':
    print('Wow, beautiful name!')
elif name == 'Pedro' or name == 'Maria' or name == 'Paulo':
    print('your name is popular in Brazil and Italy')
elif name in 'Ana Claudia Jessia Juliana':
    print = ('Nice female name!')
else:
    print('Normal name.')
print('Have great day,{}!'.format(name))