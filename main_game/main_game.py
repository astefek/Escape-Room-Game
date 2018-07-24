# Escape Room Game 

import pygame
import time
import sys
import math

# Imports
import intro
import graphics
import sudoku.puzzle
import maze.mazePuzz
import shape_puzzle
import outro



pygame.init()
pygame.font.init()

# Window/background details 
window_width = 720
window_height = 480
window = pygame.display.set_mode([window_width, window_height])

startbg = pygame.image.load('start_screenbg.png').convert()

bg = pygame.image.load('space_gamebg.png').convert()

# Font
font = pygame.font.SysFont('haettenschweiler', 90)

# Clock
clock = pygame.time.Clock()


# Mouse/Cursor 
pygame.mouse.set_cursor(*pygame.cursors.arrow)

# Progress variable 
puzzles_solved = 0


while True:
    # Start Screen
    game_loop = intro.run(window, startbg, font)
    if game_loop == 1:
        game_loop = graphics.run(window, bg)
    if game_loop == 2:
        
        outro.run(window, startbg, outro_clock)
    

 







        

