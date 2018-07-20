# Make A Shape Puzzle
# Adam
# Vassar CS Camp

import pygame
import math
import random

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

def midpoint(point1, point2):
    """Takes two points and returns the midpoint of the line between them."""
    x_coord = (point2[0] - point1[0])/2 + point1[0]
    y_coord = (point2[1] - point1[1])/2 + point1[1]
    return (x_coord, y_coord)


# Window setup
window_size = [720, 480]
window_color = pygame.Color(125, 160, 150)
window = pygame.display.set_mode(window_size)

# Generate the goal shape
shape_color = pygame.Color(75, 50, 35)

point1 = ( random.choice( range(20,130) ), random.choice( range(35,175))  )
point2 = ( random.choice( range(20, point1[0]) ), random.choice( range(176,315)) )
point3 = ( random.choice( range(20,130) ), random.choice( range(315,455)) )
point4 = ( random.choice( range(131,240)), random.choice( range(point3[1],455)) )
point5 = ( random.choice( range(240,350)), random.choice( range(315,455)) )
point6 = ( random.choice( range(point5[0],350)), random.choice( range(176,315)) )
point7 = ( random.choice( range(240,350)), random.choice( range(35,175))  )
point8 = ( random.choice( range(131,240)), random.choice( range(35,point7[1]))  )

shape_pointlist = [point1, point2, point3, point4, point5, point6, point7, point8]

# Lines for splitting up shape

linepoint_dict = {}
point_combos = [(point1, point2), (point2, point3), (point3, point4), (point4, point5), (point5, point6), (point6, point7), (point7, point8), (point8, point1)]
for combo in point_combos:
    x_coord = random.choice(range(x_min(combo[0], combo[1]), x_max(combo[0], combo[1])))
    y_coord = ( slope(combo[0], combo[1]) * (x_coord - combo[0][0]) ) + combo[0][1]
    linepoint_dict[combo] = (x_coord, y_coord)

sidepoint_list = list(linepoint_dict.values())

# Line variables (for testing)
line_color = pygame.Color(255, 225, 40)



half1 = [point1, point2, point3, point4, point4_5, point8_1]
half2 = [point8_1, point4_5, point5, point6, point7, point8]

q1 = [point8, point6, point7]
q2 = [point8, point8_1, point4_5, point5, point6]
q3 = [point1, midpoint(point8_1, point4_5), point8_1]
q4 = [point1, point2, point3, point4, point4_5, midpoint(point8_1, point4_5)]


# Main loop

while True:

    # Drawing
    window.fill(window_color)

    # Draw goal shape
    pygame.draw.polygon(window,shape_color, shape_pointlist)

    # Draw lines between points (for testing)
    #pygame.draw.lines(window, line_color, True, list(linepoint_dict.values() ) )
    for i in range(len(sidepoint_list)):
        pygame.draw.line(window, line_color, sidepoint_list[i], sidepoint_list[(i+3) % len(sidepoint_list)] )

    # User interaction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                                   # Quit
            pygame.quit()
    

    # Flip screen
    pygame.display.flip()