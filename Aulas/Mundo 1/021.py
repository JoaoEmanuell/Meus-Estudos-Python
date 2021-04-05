import pygame
print('\033[1;35mDivirtasse :)\033[m')
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()):pass