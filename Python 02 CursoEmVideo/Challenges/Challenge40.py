print('=====CHALLENGE 40=====')

note1 = float(input('Write note 1: '))
note2 = float(input('Write note 2: '))

media = (note1 + note2) / 2

if media >= 7 :
    print('Aproved!')
elif media >= 5 and media <= 6.9:
    print('Recovery!')
else:
    print('Reproved!')