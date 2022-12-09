print('=====CHALLENGE 71=====')

withdraw = int(input('Enter the withdrawal amount: '))
total = withdraw #Total amount to be decomposed
bankNotes= 100 #Take 100 dollars from the amount
totalNotes = 0
while True:
    if total >= bankNotes:
        total -= bankNotes
        totalNotes += 1
    else:
        if totalNotes > 0:
            print('Total {} notes of$ {}' .format(totalNotes, bankNotes))
        if bankNotes== 100:
            bankNotes= 50
        if bankNotes== 50:
            bankNotes= 20
        elif bankNotes== 20:
            bankNotes= 10
        elif bankNotes== 10:
            bankNotes= 5
        elif bankNotes== 5:
            bankNotes= 2
        totalNotes = 0
        if total == 0:
            break