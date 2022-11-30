print('=====CHALLENGE 24=====')

print('Create a program that reads the name of a city and says whether or not it starts with santo')

city = str(input('Enter your city name: ')).strip().lower().capitalize()

print('Santo' in city[:5])