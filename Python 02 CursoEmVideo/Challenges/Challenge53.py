print('=====CHALLENGE 53=====')

name = input('Digite uma frase: ').strip().lower()
name = name.replace(' ', '')
inverseName = name[::-1].lower()
if name == inverseName:
   print('{} e {} é palíndromo!'.format(name, inverseName))
else:
   print('{} e {} Não é palíndromo!'.format(name,inverseName))