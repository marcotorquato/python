print('=====CHALLENGE 26=====')

print("""Write a program that reads a sentence and displays:
1- How many times does the letter A appear
2- In what position does it appear the first time
3- in which position it appears last time""")

phrase = str(input('\nEnter a phrase: ')).strip().lower()

#print('\n Number of times the letter ''A'' appears: {}'.format(phrase.count('A')))
print('\nNumber of times the letter ''a'' appears: {}'.format(phrase.count('a')))

#print('\n In what position does A appear the first time: {}'.format(phrase.find('A')))
print('In what position does a appear for the first time: {}'.format(phrase.find('a')+1))

#print('\n In what position does A last appear: {}'.format(phrase.rfind('A')))
print('In what position does a last appear:{}'.format(phrase.rfind('a')+1))

