import pyautogui
from time import sleep



pyautogui.click(920,869,duration=1.5) 
pyautogui.write('Marco',duration=2)

#open file 

with open('produtos.txt', 'r') as file:
    for line in file:
        line.split(',')[0]
        product = line.split(',')[1]
        unit = line.split(',')[2]
        price = line.split(',')[3]

        #click and edit product
        pyautogui.click(259,298,duration=2)
        pyautogui.write(product)

        #click and edit unit
        pyautogui.click(259,298,duration=2)
        pyautogui.write(unit)

        #click and edit price
        pyautogui.click(259,298,duration=2)
        pyautogui.write(price)

        #button register
        pyautogui.click(907,231,duration=2)
        sleep(1)