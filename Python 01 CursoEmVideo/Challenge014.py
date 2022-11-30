print("="*5+"CHALLENGE 14"+"="*5)

print("Write a program that converts a temperature from degrees Celsius to degrees Fahrenheit")

cel = float(input('\nEnter the temperature in °C: '))

#Formula for converting from Celsius to Fahrenheit: C° * 1,800 + 32
print('\nThe temperature in degrees Fahrenheit is: {} °F' .format(cel * 1.800 + 32))

#Formula for converting from Celsius to Kelvin: C° + 273.15
print('The temperature in degrees Kelvin is: {} °K' .format(cel + 273.15))

