print(' '*39+'=====CHALLENGE 22=====')
print("""Create a program that reads a person's full name and displays:
the name with all uppercase and lowercase letters, how many letters are there in total (without considering spaces)
and how many letters are in the first name""")

name = str(input("\nEnter your first and last name: ")).strip()
divided = name.split()
print('\nYour name in all capital letters will be: {}'.format(name.upper()))
print('\nin lower case: {}'.format(name.lower()))
print('\nThe number of letters is: {}'.format(len(name) - name.count(' ')))
print('\nAnd the number of letters in your first name is: {}'.format(len(divided[0])))