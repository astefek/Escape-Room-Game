# Testing for the shape puzzle game

import pygame
import random
import time

# Initial setup
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 40)
winFont = pygame.font.SysFont( 'Arial', 30)
winScreenTime = 5
window_size = [720, 480]
window_color = pygame.Color(208, 161, 219)
window = pygame.display.set_mode(window_size)



# Function definition

def close_enough(moved_shape, win_tuple):
    """Takes a moved shape and a tuple of original shape positions and checks 
    if it fits close enough to be counted as a win."""
    matches = 0
    for win_shape in win_tuple:
        for vertex in moved_shape:
            for x_leeway in range(-5,5):
                for y_leeway in range(-5,5):
                    if (vertex[0] + x_leeway, vertex[1] + y_leeway) in win_shape:
                        matches += 1
    if matches >= len(win_shape):
        return 1
    else: return 0

def move_shape(shape, dir):
    """Takes a pointlist of a shape and returns a new shape pointlist 1 pixel 
    to the given direction."""
    new_shape = []
    for vertex in shape:
        if dir == 'left':
            new_vertex = (vertex[0] - 1, vertex[1])
        elif dir == 'right':
            new_vertex = (vertex[0] + 1, vertex[1])
        elif dir == 'up':
            new_vertex = (vertex[0], vertex[1] - 1)
        elif dir == 'down':
            new_vertex = (vertex[0], vertex[1] + 1)
        new_shape += [ new_vertex ]
    return(new_shape)
        
def midpoint(point1, point2):
    """Takes two points and returns the midpoint of the line between them."""
    x_coord = (point2[0] - point1[0])/2 + point1[0]
    y_coord = (point2[1] - point1[1])/2 + point1[1]
    return [x_coord, y_coord]

def move_to_side(pointlist):
    """Takes a list of points and adjusts their coordinates."""
    newpointlist = []
    for point in pointlist:
        newpoint0 = point[0] + 340
        newpoint1 = point[1]
        newpointlist += [(newpoint0, newpoint1)]
    return newpointlist

def random_pos(pointlist):
    """Takes a list of points making a polygon on the right side of the screen
    and randomly translates the polygon."""
    newpointlist = []
    x_mix = random.choice(range(-200, 200))
    y_mix = random.choice(range(-200, 200))
    for point in pointlist:
        newpointx = point[0] + x_mix
        newpointy = point[1] + y_mix
        newpointlist += [(newpointx, newpointy)]
    return newpointlist

def reset_num_colors():
    """Returns eight instances of (0,0,0)"""
    return (0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)

def run(window, puzzles_solved):
    """Creates all necessary variables and runs shape game."""

    wait_time = 0.003

    # Generate the goal shape
    shape_color = pygame.Color(0,0,0)

    point1 = ( random.choice( range(20,130) ), random.choice( range(60,175))  )
    point2 = ( random.choice( range(20, point1[0]) ), random.choice( range(176,315)) )
    point3 = ( random.choice( range(20,130) ), random.choice( range(315,455)) )
    point4 = ( random.choice( range(131,240)), random.choice( range(point3[1],455)) )
    point5 = ( random.choice( range(240,330)), random.choice( range(315,455)) )
    point7 = ( point5[0] + 20, random.choice( range(60,175))  )
    point6 = ( random.choice( range(point5[0],point7[0])), random.choice( range(176,315)) )
    point8 = ( random.choice( range(131,240)), random.choice( range(60,point7[1]))  )
    shape_pointlist = [point1, point2, point3, point4, point5, point6, point7, point8]


    # Splitting the goal shape into eight parts
    point4_5 = midpoint(point4, point5)
    point8_1 = midpoint(point8, point1)
    
    e1 = move_to_side([point8, point6, point7])
    e2 = move_to_side([point8_1, midpoint(point8_1, point4_5), point6])
    e3 = move_to_side([point8_1, point6, point8])
    e4 = move_to_side([midpoint(point8_1, point4_5), point4_5, point5, point6])
    e5 = move_to_side([point1, point2, point4_5, midpoint(point4_5, point8_1)])
    e6 = move_to_side([point1, midpoint(point8_1, point4_5), point8_1])
    e7 = move_to_side([point2, point3, point4_5])
    e8 = move_to_side([point3, point4, point4_5])

    # Make win shape tuples
    # 3 vertex win shapes
    three_win_shapes = ([point8, point6, point7], [tuple(point8_1), tuple(midpoint(point8_1, point4_5)), point6], \
    [tuple(point8_1), point6, point8], [point1, tuple(midpoint(point8_1, point4_5)), tuple(point8_1)], \
    [point2, point3, tuple(point4_5)], [point3, point4, tuple(point4_5)])

    # 4 vertex win shapes
    four_win_shapes = ([tuple(midpoint(point8_1, point4_5)), tuple(point4_5), point5, point6], \
    [point1, point2, tuple(point4_5), tuple(midpoint(point4_5, point8_1))])


    # Disperse shapes
    subshape_list = [e1, e2, e3, e4, e5, e6, e7, e8]
    indiv_shapes = {}
    available_colors = [pygame.Color(255, 45, 40), pygame.Color(255, 230, 17), pygame.Color(28, 185, 65), pygame.Color(45, 255, 25), \
    pygame.Color(40, 45, 210), pygame.Color(30, 205, 220) , pygame.Color(255, 113, 29), pygame.Color(170, 28, 186)]

    for sub_shape in subshape_list:
        while True:
            neweighth = random_pos(sub_shape)
            errors = 0
            for point in neweighth:
                if point[0] <= 350 or point[0] >= 720 or point[1] <= 60 or point[1] >= 480:
                    errors += 1
            if errors == 0:
                index = random.choice(range(len(available_colors)))
                indiv_shapes[tuple(neweighth)] = available_colors[index]
                available_colors = available_colors[:index] + available_colors[:index:-1]
                break

    # Assign shapes to numbers
    selector_numbers = {}
    available_shapes = []
    for shape in indiv_shapes:
        available_shapes.append(shape)

    for num in range(8):
        index = random.choice(range(len(available_shapes)))
        selector_numbers[num] = available_shapes[index]
        available_shapes = available_shapes[:index] + available_shapes[index+1::]

    # Make selector boxes
    box_pos = [[20 + x, 10] for x in range(0, 510, 70)]
    box_dim = [50, 50]
    current_num = 0

    # Win message
    winMessage = winFont.render('Congratulations!', False, (110, 105, 50) )

    # Beginning direction variable definition
    right = False
    left = False
    up = False
    down = False

    while True:

        # Initial number colors
        oneColor, twoColor, threeColor, fourColor, fiveColor, sixColor, sevenColor, eightColor = reset_num_colors()
        oneColor = (255,255,255)

        # Change selector number color
        if current_num == 0:
            oneColor, twoColor, threeColor, fourColor, fiveColor, sixColor, sevenColor, eightColor = reset_num_colors()
            oneColor = (255,255,255)
        elif current_num == 1:
            oneColor, twoColor, threeColor, fourColor, fiveColor, sixColor, sevenColor, eightColor = reset_num_colors()
            twoColor = (255,255,255)
        elif current_num == 2:
            oneColor, twoColor, threeColor, fourColor, fiveColor, sixColor, sevenColor, eightColor = reset_num_colors()
            threeColor = (255,255,255)
        elif current_num == 3:
            oneColor, twoColor, threeColor, fourColor, fiveColor, sixColor, sevenColor, eightColor = reset_num_colors()
            fourColor = (255,255,255)
        elif current_num == 4:
            oneColor, twoColor, threeColor, fourColor, fiveColor, sixColor, sevenColor, eightColor = reset_num_colors()
            fiveColor = (255,255,255)
        elif current_num == 5:
            oneColor, twoColor, threeColor, fourColor, fiveColor, sixColor, sevenColor, eightColor = reset_num_colors()
            sixColor = (255,255,255)
        elif current_num == 6:
            oneColor, twoColor, threeColor, fourColor, fiveColor, sixColor, sevenColor, eightColor = reset_num_colors()
            sevenColor = (255,255,255)
        elif current_num == 7:
            oneColor, twoColor, threeColor, fourColor, fiveColor, sixColor, sevenColor, eightColor = reset_num_colors()
            eightColor = (255,255,255)

        # Num definition            
        oneSurface   = font.render('1', False, oneColor )
        twoSurface   = font.render('2', False, twoColor )
        threeSurface = font.render('3', False, threeColor )
        fourSurface  = font.render('4', False, fourColor )
        fiveSurface  = font.render('5', False, fiveColor )
        sixSurface   = font.render('6', False, sixColor )
        sevenSurface = font.render('7', False, sevenColor )
        eightSurface = font.render('8', False, eightColor )
        
        # Number boxes 
        box_nums = [oneSurface, twoSurface, threeSurface, fourSurface, fiveSurface, sixSurface, sevenSurface, eightSurface]


        # Drawing
        window.fill(window_color)

        # Draw goal shape
        for point in shape_pointlist:
            pygame.draw.circle(window, shape_color, point, 3)

        # Draw sub_shapes
        for shape in indiv_shapes:
            pygame.draw.polygon(window, indiv_shapes[shape] , shape)

        # Draw selector boxes
        for box in range(len(box_pos)):
            pygame.draw.rect(window, indiv_shapes[selector_numbers[box]] , box_pos[box] + box_dim)
            window.blit( box_nums[box], ( box_pos[box][0] + 14, box_pos[box][1] + 3 ) )


        # User interaction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                                                           # Quit
                pygame.quit()    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return puzzles_solved
                elif event.key == pygame.K_1:                                                     # Selector box movement
                    current_num = 0
                elif event.key == pygame.K_2:
                    current_num = 1
                elif event.key == pygame.K_3:
                    current_num = 2
                elif event.key == pygame.K_4:
                    current_num = 3
                elif event.key == pygame.K_5:
                    current_num = 4
                elif event.key == pygame.K_6:
                    current_num = 5
                elif event.key == pygame.K_7:
                    current_num = 6
                elif event.key == pygame.K_8:
                    current_num = 7
                elif event.key == pygame.K_RIGHT:                                                   # Shape movement
                    right = True
                elif event.key == pygame.K_LEFT:
                    left = True
                elif event.key == pygame.K_UP:
                    up = True
                elif event.key == pygame.K_DOWN:
                    down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:                                                  
                    right = False
                elif event.key == pygame.K_LEFT:
                    left = False
                elif event.key == pygame.K_UP:
                    up = False
                elif event.key == pygame.K_DOWN:
                    down = False

        if right:                                                                                 # Shape movement
            for shape in indiv_shapes:
                if shape == selector_numbers[current_num]:
                    indiv_shapes[tuple(move_shape(shape,'right'))] = indiv_shapes[shape]
                    indiv_shapes.pop(shape)
                    selector_numbers[current_num] = tuple(move_shape(shape, 'right'))
                    break
        if left:
            for shape in indiv_shapes:
                if shape == selector_numbers[current_num]:
                    indiv_shapes[tuple(move_shape(shape,'left'))] = indiv_shapes[shape]
                    indiv_shapes.pop(shape)
                    selector_numbers[current_num] = tuple(move_shape(shape, 'left'))
                    break
        if up:
            for shape in indiv_shapes:
                if shape == selector_numbers[current_num]:
                    indiv_shapes[tuple(move_shape(shape,'up'))] = indiv_shapes[shape]
                    indiv_shapes.pop(shape)
                    selector_numbers[current_num] = tuple(move_shape(shape, 'up'))
                    break
        if down:
            for shape in indiv_shapes:
                if shape == selector_numbers[current_num]:
                    indiv_shapes[tuple(move_shape(shape,'down'))] = indiv_shapes[shape]
                    indiv_shapes.pop(shape)
                    selector_numbers[current_num] = tuple(move_shape(shape, 'down'))
                    break

        # Flip screen
        pygame.display.flip()
        time.sleep(wait_time)

        # Win condition
        correct_shapes = 0

        # Check if game is won
        for shape in indiv_shapes:
            if len(shape) == 4:
                correct_shapes += close_enough(shape, four_win_shapes)
            elif len(shape) == 3:
                correct_shapes += close_enough(shape, three_win_shapes)

        # If game is won
        if correct_shapes == 8:
            window.blit(winMessage, (485, 60) )
            pygame.display.flip()
            time.sleep(winScreenTime)
            return puzzles_solved + 1
