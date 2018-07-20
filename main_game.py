# Escape Room Game 

import pygame
import time
import sys
import math

# Imports
import start_screen
import graphics
import sudoku
import maze

pygame.init()
pygame.font.init()

# Window/background details 
window_width = 720
window_height = 480
window = pygame.display.set_mode([window_width, window_height])


window.blit(bg, (0,0))

# Mouse/Cursor 
pygame.mouse.set_cursor(*pygame.cursors.arrow)


while True:   
    # Start Screen
    start_screen.run(window)

    # Main Loop - graphics
    graphics.run(window)








        

