print('=====CHALLENGE 55=====')

list = []
for w in range(0, 5):
    weight = float(input('Digite o weight: '))
    list.append(weight) # ".append" add the value to the index.
print('The weight larger  is {}Kg'.format(max(list))) # "max()" shows the larger value of the index.
print('The weight smaller is {}Kg' .format(min(list))) # "min()" shows the smallest value of the index.
