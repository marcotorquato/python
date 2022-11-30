print('=====CHALLENGE 29=====\n'
      
      'Write a program that reads the speed of a car\n'
      'If he exceeds 80km/h, show a message saying he has been fined\n'
      'The fine will cost R$7.00 for each km over the limit.\n')

speed = int(input('Enter the speed of the car:'))

if speed > 80:
    print('You were fined in: R${:.2f}'.format((speed - 80)*7))
else:
    print('Keep driving carefully, have a nice day! :)')
