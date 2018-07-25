# Escape Room Game
#
# Vassar CS Camp

import pygame
import math
import random
import sudoku.sudoku_generator as sudoku_generator
import time

# 6 x 6 sudoku
# 1-6 in every row
# 1-6 in every column

pygame.init()
pygame.font.init()
font = pygame.font.SysFont( 'Arial', 40)
winFont = pygame.font.SysFont( 'Arial', 30)
winScreenTime = 5

# Window setup

window_size = [720, 480]
window_color = pygame.Color(200, 160, 180)
window = pygame.display.set_mode(window_size)

# Grid box vertices

box_pos = [ [ [30 + y, 30 + x] for x in range(0, 390, 72) ] for y in range(0, 390, 72) ]

box_dim = [60, 60]
box_color = pygame.Color(244 , 237, 231)


# Image assignments

oneSurface   = font.render('1', False, (74,110,85) )
twoSurface   = font.render('2', False, (74,110,85) )
threeSurface = font.render('3', False, (74,110,85) )
fourSurface  = font.render('4', False, (74,110,85) )
fiveSurface  = font.render('5', False, (74,110,85) )
sixSurface   = font.render('6', False, (74,110,85) )

redOneSurface   = font.render('1', False, (235,45,45) )
redTwoSurface   = font.render('2', False, (235,45,45) )
redThreeSurface = font.render('3', False, (235,45,45) )
redFourSurface  = font.render('4', False, (235,45,45) )
redFiveSurface  = font.render('5', False, (235,45,45) )
redSixSurface   = font.render('6', False, (235,45,45) ) 

winMessage = winFont.render('Congratulations!', False, (240, 190, 40) )


# Halo around selected box

selector_pointlist = [ [30, 30], [30, 90], [90, 90], [90, 30] ]
selector_color = pygame.Color(169, 205, 117)
selector_width = 5


# Function definitions 

def draw_box(surface, color, Rect):
    """Draws a box"""
    pygame.draw.rect(surface, color, Rect)

def numToImage(n):
    """Takes an integer 1 to 6 and returns the image of that number"""
    if n == 1:
        return oneSurface
    elif n == 2:
        return twoSurface
    elif n == 3:
        return threeSurface
    elif n == 4:
        return fourSurface
    elif n == 5:
        return fiveSurface
    elif n == 6:
        return sixSurface

def redToNorm(redn):
    """Takes a red number and returns the normal color number"""
    if redn == redOneSurface:
        return oneSurface
    elif redn == redTwoSurface:
        return twoSurface
    elif redn == redThreeSurface:
        return threeSurface
    elif redn == redFourSurface:
        return fourSurface
    elif redn == redFiveSurface:
        return fiveSurface
    elif redn == redSixSurface:
        return sixSurface

def validMove(direction):
    """Takes a direction and returns True if the selector can move that 
    direction or False if it will leave the grid."""
    if direction == 'up':
        if selector_pointlist[0][1] == 30:
            return False
    elif direction == 'down':
        if selector_pointlist[2][1] == 450:
            return False 
    elif direction == 'right':
        if selector_pointlist[2][0] == 450:
            return False
    elif direction == 'left':
        if selector_pointlist[0][0] == 30:
            return False
    return True

def boxFromSelector(selector_pointlist):
    """Takes selector vertices and returns the box that is being selected"""
    for box in grid_dict:
        if box[0] == selector_pointlist[0][0] and \
        box[1] == selector_pointlist[0][1]:
            return box

def imageToNum(image):
    """Takes a number image and returns its number.
    Does not work with red numbers."""
    if image == oneSurface:
        return 1
    elif image == twoSurface:
        return 2
    elif image == threeSurface:
        return 3
    elif image == fourSurface:
        return 4
    elif image == fiveSurface:
        return 5
    elif image == sixSurface:
        return 6

def makeSolutionGrid(d):
    """Takes a full dictionary of box locations and regular numbers.
    Returns a grid (list of lists) corresponding to the current 
    sudoku solutions."""
    column1 = [ d[(30,30)], d[(30, 102)], d[(30,174)], d[(30, 246)], d[(30, 318)], d[(30, 390)] ]
    column2 = [ d[(102,30)], d[(102, 102)], d[(102,174)], d[(102, 246)], d[(102, 318)], d[(102, 390)] ]
    column3 = [ d[(174,30)], d[(174, 102)], d[(174,174)], d[(174, 246)], d[(174, 318)], d[(174, 390)] ]
    column4 = [ d[(246,30)], d[(246, 102)], d[(246,174)], d[(246, 246)], d[(246, 318)], d[(246, 390)] ]
    column5 = [ d[(318,30)], d[(318, 102)], d[(318,174)], d[(318, 246)], d[(318, 318)], d[(318, 390)] ]
    column6 = [ d[(390,30)], d[(390, 102)], d[(390,174)], d[(390, 246)], d[(390, 318)], d[(390, 390)] ]
    grid = [column1, column2, column3, column4, column5, column6]
    return grid



# gen grid values dictionary
grid_dict = {}
values_grid = sudoku_generator.make_puzzle()
sudoku_generator.display_grid(values_grid)          # for comparison display it in terminal

for x in range( len(box_pos) ):
    for y in range( len(box_pos)):
        grid_dict[ tuple(box_pos[x][y]) ] = numToImage( values_grid[x][y] )


# Choose which boxes to fill
rand_filled_boxes = {}                                                # Starting boxes
available_keys = list(grid_dict.keys())
for x in range(14):                                                   # Num boxes pre-filled
    box_selection = random.choice(available_keys)
    rand_filled_boxes[box_selection] = grid_dict[box_selection]
    for i in range(len(available_keys)):
        if available_keys[i] == box_selection: loc = i
    available_keys = available_keys[:loc] + available_keys[:loc:-1]




 # Main loop
def run(window):
    """Runs sudoku"""
    player_filled = {}
    win = False
    while True:

        # Drawing

        window.fill(window_color)
        
        # Draw grid boxes
        for x in range( len(box_pos) ):
            for y in range( len(box_pos[x]) ):
                draw_box(window, box_color, box_pos[x][y] + box_dim)

        # Fill in grid with numbers
        for box in rand_filled_boxes:
            window.blit( grid_dict[box], ( box[0] + 18, box[1] + 10 ) )

        pygame.draw.polygon(window, selector_color, selector_pointlist, selector_width)

        # Draw grid lines
        #horizontal line
        pygame.draw.line(window, pygame.Color(138, 120, 115), (30, 239), (450,239), 8 )
        #vertical lines
        pygame.draw.line(window, pygame.Color(138, 120, 115), (167, 30), (167,450), 8 )
        pygame.draw.line(window, pygame.Color(138, 120, 115), (311, 30), (311,450), 8 )

        #Draw user inputted numbers
        for box in player_filled:
            window.blit( player_filled[box], ( box[0] + 18, box[1] + 10 ) )


        # User interactions

        for event in pygame.event.get():
            if event.type == pygame.QUIT:                                   # Quit
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and validMove('up'):            # Selector movement
                    for vertex in range(4):
                        selector_pointlist[vertex][1] -= 72
                elif event.key == pygame.K_DOWN and validMove('down'):
                    for vertex in range(4):
                        selector_pointlist[vertex][1] += 72
                elif event.key == pygame.K_RIGHT and validMove('right'):
                    for vertex in range(4):
                        selector_pointlist[vertex][0] += 72
                elif event.key == pygame.K_LEFT and validMove('left'):
                    for vertex in range(4):
                        selector_pointlist[vertex][0] -= 72
                
                elif event.key == pygame.K_1:                              # Inputting numbers
                    current_box = boxFromSelector(selector_pointlist)
                    if current_box not in rand_filled_boxes:
                        player_filled[current_box] = redOneSurface
                elif event.key == pygame.K_2:
                    current_box = boxFromSelector(selector_pointlist)
                    if current_box not in rand_filled_boxes:
                        player_filled[current_box] = redTwoSurface
                elif event.key == pygame.K_3:
                    current_box = boxFromSelector(selector_pointlist)
                    if current_box not in rand_filled_boxes:
                        player_filled[current_box] = redThreeSurface
                elif event.key == pygame.K_4:
                    current_box = boxFromSelector(selector_pointlist)
                    if current_box not in rand_filled_boxes:
                        player_filled[current_box] = redFourSurface
                elif event.key == pygame.K_5:
                    current_box = boxFromSelector(selector_pointlist)
                    if current_box not in rand_filled_boxes:
                        player_filled[current_box] = redFiveSurface
                elif event.key == pygame.K_6:
                    current_box = boxFromSelector(selector_pointlist)
                    if current_box not in rand_filled_boxes:
                        player_filled[current_box] = redSixSurface
                elif event.key == pygame.K_SPACE:
                    player_filled = {}
                elif event.key == pygame.K_BACKSPACE:
                    try:
                        player_filled.pop(current_box)
                    except:
                        pass
                elif event.key == pygame.K_ESCAPE:
                    return False

                    
        # Flip Screen
        pygame.display.flip()

        # Win Condition

        if win:
            window.blit(winMessage, (485, 30) )
            pygame.display.flip()
            time.sleep(winScreenTime)
            return True

        player_soln = {}
        for box in rand_filled_boxes:
            player_soln[box] = imageToNum( rand_filled_boxes[box] )
        for box in player_filled:
            player_soln[box] = imageToNum( redToNorm(player_filled[box]) )
        if len(player_soln) == 36:
            win = True
            for x in range(6):
                for y in range(6):
                    solution_grid = makeSolutionGrid(player_soln)
                    xy = solution_grid[x][y]
                    solution_grid[x][y] = 0
                    if not sudoku_generator.validMove(x, y, xy, solution_grid):
                        win = False