# Escape Room Game
#
# Vassar CS Camp

import pygame
import math
import random

# 6 x 6 sudoku
# 1-6 in every row
# 1-6 in every column

pygame.init()

# Window setup

window_size = [720, 480]
window_color = pygame.Color(200, 130, 165)
window = pygame.display.set_mode(window_size)

# Grid box vertices

box_pos11 = [30, 30]
box_pos12 = [30, 102]
box_pos13 = [30, 174]
box_pos14 = [30, 246]
box_pos15 = [30, 318]
box_pos16 = [30, 390]

box_pos21 = [102, 30]
box_pos22 = [102, 102]
box_pos23 = [102, 174]
box_pos24 = [102, 246]
box_pos25 = [102, 318]
box_pos26 = [102, 390]

box_pos31 = [174, 30]
box_pos32 = [174, 102]
box_pos33 = [174, 174]
box_pos34 = [174, 246]
box_pos35 = [174, 318]
box_pos36 = [174, 390]

box_pos41 = [246, 30]
box_pos42 = [246, 102]
box_pos43 = [246, 174]
box_pos44 = [246, 246]
box_pos45 = [246, 318] 
box_pos46 = [246, 390]

box_pos51 = [318, 30]
box_pos52 = [318, 102]
box_pos53 = [318, 174]
box_pos54 = [318, 246]
box_pos55 = [318, 318]
box_pos56 = [318, 390]

box_pos61 = [390, 30]
box_pos62 = [390, 102]
box_pos63 = [390, 174]
box_pos64 = [390, 246]
box_pos65 = [390, 318]
box_pos66 = [390, 390]

box_dim = [60, 60]
box_color = pygame.Color(255 , 255, 255)

# Number images

pygame.image.fromstring('1', [50,50], )


def draw_box(surface, color, Rect):
    """Draws a box"""
    pygame.draw.rect(surface, color, Rect)


 # Main loop

while True:

    window.fill(window_color)
    
    # Drawing all boxes in the grid
    draw_box(window, box_color, box_pos11 + box_dim)
    draw_box(window, box_color, box_pos12 + box_dim)
    draw_box(window, box_color, box_pos13 + box_dim)
    draw_box(window, box_color, box_pos14 + box_dim)
    draw_box(window, box_color, box_pos15 + box_dim)
    draw_box(window, box_color, box_pos16 + box_dim)
    draw_box(window, box_color, box_pos21 + box_dim)
    draw_box(window, box_color, box_pos22 + box_dim)
    draw_box(window, box_color, box_pos23 + box_dim)
    draw_box(window, box_color, box_pos24 + box_dim)
    draw_box(window, box_color, box_pos25 + box_dim)
    draw_box(window, box_color, box_pos26 + box_dim)
    draw_box(window, box_color, box_pos31 + box_dim)
    draw_box(window, box_color, box_pos32 + box_dim)
    draw_box(window, box_color, box_pos33 + box_dim)
    draw_box(window, box_color, box_pos34 + box_dim)
    draw_box(window, box_color, box_pos35 + box_dim)
    draw_box(window, box_color, box_pos36 + box_dim)
    draw_box(window, box_color, box_pos41 + box_dim)
    draw_box(window, box_color, box_pos42 + box_dim)
    draw_box(window, box_color, box_pos43 + box_dim)
    draw_box(window, box_color, box_pos44 + box_dim)
    draw_box(window, box_color, box_pos45 + box_dim)
    draw_box(window, box_color, box_pos46 + box_dim)
    draw_box(window, box_color, box_pos51 + box_dim)
    draw_box(window, box_color, box_pos52 + box_dim)
    draw_box(window, box_color, box_pos53 + box_dim)
    draw_box(window, box_color, box_pos54 + box_dim)
    draw_box(window, box_color, box_pos55 + box_dim)
    draw_box(window, box_color, box_pos56 + box_dim)
    draw_box(window, box_color, box_pos61 + box_dim)
    draw_box(window, box_color, box_pos62 + box_dim)
    draw_box(window, box_color, box_pos63 + box_dim)
    draw_box(window, box_color, box_pos64 + box_dim)
    draw_box(window, box_color, box_pos65 + box_dim)
    draw_box(window, box_color, box_pos66 + box_dim)
    



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    pygame.display.flip()



