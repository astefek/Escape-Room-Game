# Make A Shape Puzzle
# Adam
# Vassar CS Camp

import pygame
import math
import random

### MAYBE CHANGE SHAPE DRAWING SO THAT ALL ANGLES CANT BE CONVEX??? ELIMINATE LINE OUTSIDE SHAPE PROBLEM
###
###
###



# Function definition
def x_min(point1, point2):
    """Returns the min x value of the two given points"""
    smaller_x = min([point1[0], point2[0]])
    return smaller_x

def y_min(point1, point2):
    """Returns the min y value of the two given points."""
    smaller_y = min([point1[1], point2[1]])
    return smaller_y

def y_max(point1, point2):
    """Returns the max y value of two given points."""
    larger_y  = max([point1[1], point2[1]])
    return larger_y

def x_max(point1, point2):
    """Returns the max x value of two given points.""" 
    larger_x  = max([point1[0], point2[0]])
    return larger_x

def slope(point1, point2):
    """Takes two points and returns the slope of the line between them."""
    numerator = point2[1] - point1[1]
    denominator = point2[0] - point1[0]
    return numerator/denominator

    

# Window setup
window_size = [720, 480]
window_color = pygame.Color(125, 160, 150)
window = pygame.display.set_mode(window_size)

# Generate the goal shape
shape_color = pygame.Color(75, 50, 35)

point1 = ( random.choice( range(20,130) ), random.choice( range(35,175))  )
point2 = ( random.choice( range(20,130) ), random.choice( range(176,315)) )
point3 = ( random.choice( range(20,130) ), random.choice( range(315,455)) )
point4 = ( random.choice( range(131,240)), random.choice( range(315,455)) )
point5 = ( random.choice( range(240,350)), random.choice( range(315,455)) )
point6 = ( random.choice( range(240,350)), random.choice( range(176,315)) )
point7 = ( random.choice( range(240,350)), random.choice( range(35,175))  )
point8 = ( random.choice( range(131,240)), random.choice( range(35,175))  )

shape_pointlist = [point1, point2, point3, point4, point5, point6, point7, point8]

# Lines for splitting up shape

linepoint_dict = {}
point_combos = [(point1, point2), (point2, point3), (point3, point4), (point4, point5), (point5, point6), (point6, point7), (point7, point8), (point8, point1)]
for combo in point_combos:
    x_coord = random.choice(range(x_min(combo[0], combo[1]), x_max(combo[0], combo[1])))
    y_coord = ( slope(combo[0], combo[1]) * (x_coord - combo[0][0]) ) + combo[0][1]
    linepoint_dict[combo] = (x_coord, y_coord)


# Line variables (for testing)
line_color = pygame.Color(255, 225, 40)


# Test print section
print(list(linepoint_dict.values()))

# Main loop

while True:

    # Drawing
    window.fill(window_color)

    # Draw goal shape
    pygame.draw.polygon(window,shape_color, shape_pointlist)

    # Draw lines between points (for testing)
    pygame.draw.lines(window, line_color, True, list(linepoint_dict.values() ) )


    # User interaction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                                   # Quit
            pygame.quit()
    

    # Flip screen
    pygame.display.flip()