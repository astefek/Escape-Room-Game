import pygame


pygame.init()

window_width = 720
window_height = 480

map_width = 36
map_height = 24

window = pygame.display.set_mode([window_width, window_height])

bg = pygame.image.load('space_gamebg.png').convert()

window.blit(bg, (0,0))


pygame.display.flip()

while True:
    pass
   
    





