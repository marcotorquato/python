print('=====CHALLENGE 69=====')

over_18 = total_men = total_women = under_20 = 0
answer =  ''#variable of control

while answer != 'N': #while the answer is not 'N' continue to execute the code

   age = int(input('Write age: '))
   sexo = input('Write sex [M/F]').upper().strip()

   if age > 18: #check if there are people over 18 years
       over_18 += 1 #counts how many people are over 18

   if sexo == 'M': #if the sex is equal to the male who receives the value of 'M'
       total_men += 1 #store this count and then display to know how many men have

   if sexo == 'F': #if the sex is equal to Femi that receives the value of 'F'
        total_women += 1  #store this count and then display to know how many women have
        if age < 20:
            under_20 += 1

   answer = input('Wishes to continue ? [S/N]: ').upper().strip()[0]

print()

print('End of Registration')
print()
print(f'People over 18: {over_18}')
print(f'Men registered: {total_men}')
print(f'Women registered: {total_women}')
print(f'Registered Women under 20 years: {under_20}')