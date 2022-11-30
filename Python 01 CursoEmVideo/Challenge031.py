print('=====CHALLENGE 31=====\n'

      'Develop a program that asks the distance of a trip in km.\n'
      'Calculate the price of a ticket, charging R$0.50 per KM for trips of up to 200km\n'
      'And R$0.45 for longer trips\n')

travel = int(input('Enter the distance in Kilometers of the trip:'))

above = 0.45
eq_o_un = 0.50

if travel <= 200:
    print('The cost of the trip was: R${:.2f}'.format((eq_o_un*travel)))
else:
    print('The value of the trip was: R${:.2f}'.format(above*travel))
