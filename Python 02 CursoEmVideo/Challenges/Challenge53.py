print('=====CHALLENGE 53=====')

name = input('Write a phrase: ').strip().lower()
words= name.split()
together = ''.join(words)
inverseName = ''

for letter in range (len(together) -1, -1, -1):
   inverseName += together[letter]
if inverseName == together:
   print(' Palindromo TRUE ')
else:
   print('Palidromo OFF')