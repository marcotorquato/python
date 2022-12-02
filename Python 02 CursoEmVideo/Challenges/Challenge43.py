print('=====CHALLENGE 43=====')

weight = float(input('What is your current weight in KG? '))
height = float(input('How tall are you meters? '))

imc = weight / (height ** 2)

print('Your IMC is: %.4f' %imc)

if imc < 18.5:
    print('You are underweight!')
elif imc > 18.5 and imc < 25:
    print('You are at the ideal weight!')
elif imc > 25 and imc < 30:
    print('You are overweight!')
elif imc > 30 and imc < 40:
    print('Obesity!')
else:
    print('Morbid obesity')