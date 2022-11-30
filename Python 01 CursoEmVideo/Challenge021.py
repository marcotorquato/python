print('=====CHALLENGE 21=====')

print('Make a python program that opens and plays the audio from an mp3 file')

import pygame
pygame.init()
pygame.mixer.music.load('aha.mp3')
pygame.mixer.music.play()
pygame.event.wait()
