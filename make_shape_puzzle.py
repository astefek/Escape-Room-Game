# Make A Shape Puzzle
# Adam
# Vassar CS Camp

import pygame
import math
import random

# Function definition


# Window setup
window_size = [720, 480]
window_color = pygame.Color(125, 160, 150)
window = pygame.display.set_mode(window_size)

# Generate the goal shape
shape_color = pygame.Color(115, 50, 40)

point1 = ( random.choice( range(20,130) ), random.choice( range(35,175))  )
point2 = ( random.choice( range(20,130) ), random.choice( range(315,455)) )
point3 = ( random.choice( range(240,350)), random.choice( range(315,455)) )
point4 = ( random.choice( range(240,350)), random.choice( range(35,175))  )


shape_pointlist = [point1, point2, point3, point4]

additional_point_spaces = [ [range(21,130), range(176,315)], [range(240,350), range(176,315)], \
[range(131,240), range(35,175)], [range(131,240), range(315, 455)] ]

num_additional_points = random.choice(range(5))
loc_list = [0, 1, 2, 3]
for n in range(num_additional_points):
    loc = random.choice(loc_list)
    new_point = [random.choice(additional_point_spaces[loc][0]), random.choice(additional_point_spaces[loc][1])]
    added_point = tuple(new_point)
    if loc == 0:
    

print(shape_pointlist)


# Main loop

while True:

    # Drawing
    window.fill(window_color)

    # Draw goal shape
    pygame.draw.polygon(window,shape_color, shape_pointlist)

    # User interaction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                                   # Quit
            pygame.quit()
    

    # Flip screen
    pygame.display.flip()