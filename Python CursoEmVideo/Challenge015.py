print('=====CHALLENGE 015=====')

print("Write a program that asks the number of kilometers traveled by a rental car and the number of days "
      "for which it was rented. Calculate the price to pay, knowing that the car costs R$60 per day and R$0,"
      "15 per km driven.")

days = int(input('\nNumber of days rented: '))* 60
km = int(input('Number of kilometers driven: '))* 0.15

print('The total to be paid is: R${:.2f}'.format(days + km))
