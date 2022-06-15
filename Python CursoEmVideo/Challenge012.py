print('=====CHALLENGE 12=====')

print('\nMake an algorithm that reads the price of a product and displays its new price with a 5% discount')

product = float(input('Enter the product value: '))
disc = product - (product * 0.05)
vdisc = product * 0.05


print('The value of the product with a 5 percent discount is: R${:.2f}'.format(disc))
print('The discounted price of the product was: R${:.2f}'.format(vdisc))