import pyautogui
from time import sleep



pyautogui.click(920,869,duration=1.5) 
pyautogui.write('Marco',duration=2)

#open file 

with open('produtos.txt', 'r') as file:
    for line in file:
        line.split(,)