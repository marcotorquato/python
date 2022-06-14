print('=====DESAFIO 08=====')
print('\nEscreva um programa que leia um valor em metros e o exiba convertido em todas as medidas.')
num = float(input('Digite o valor da metragem:'))
dm = num * 10
cm = num * 100
mm = num * 1000
dam = num / 10
hm = num / 100 #hectômetro
km = num / 1000
print('\nO valor: {}m \nem milímetro: {:.0f}mm\nem centímero: {:.0f}cm\nem decímetro: {:.0f}dm \nem decâmetro: {}dam\nem hectômetro: {}hm\ne em kilometro: {}km'.format(num, mm, cm, dm, dam, hm, km))
