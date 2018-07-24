# Ascii sudoku 6x6
#
#
import random

def gen_grid():
    """Generates an empty 6 x 6 grid. Empty cells are represented with '.'"""
    
    LoL = [ [0 for x in range(6)] for x in range(6) ]
    return LoL


def validMove(x, y, num, grid):
    """Checks if assigning num to LoL[x][y] is a valid move. Returns True
    if valid, and False if not."""

    # Check column
    for i in range(6):
        if grid[x][i] == num:
            return False
    
    # Check row
    for i in range(6):
        if grid[i][y] == num:
            return False
    
    # Check sub-cell
    if x in [0,1]:
        if y in [0,1,2]:
            for xcell in [0,1]:
                for ycell in [0,1,2]:
                    if grid[xcell][ycell] == num:
                        return False
        elif y in [3,4,5]:
            for xcell in [0,1]:
                for ycell in [3,4,5]:
                    if grid[xcell][ycell] == num:
                        return False
    elif x in [2,3]:
        if y in [0,1,2]:
            for xcell in [2,3]:
                for ycell in [0,1,2]:
                    if grid[xcell][ycell] == num:
                        return False
        elif y in [3,4,5]:
            for xcell in [2,3]:
                for ycell in [3,4,5]:
                    if grid[xcell][ycell] == num:
                        return False
    elif x in [4,5]:
        if y in [0,1,2]:
            for xcell in [4,5]:
                for ycell in [0,1,2]:
                    if grid[xcell][ycell] == num:
                        return False
        elif y in [3,4,5]:
            for xcell in [4,5]:
                for ycell in [3,4,5]:
                    if grid[xcell][ycell] == num:
                        return False

    return True
    

def fill_cell(x, y, grid):
    """Assigns a number to a cell in the grid"""
    options = [1,2,3,4,5,6]
    tries = 0

    while True:
        tries += 1
        if tries > 6:
            grid[x][y] = '@'
            return
        assignment = random.choice(options)
        if validMove(x, y, assignment, grid):
            grid[x][y] = assignment
            break
        else:
            for i in range( len(options) ):
                if options[i] == assignment: loc = i
            options = options[0:loc] + options[loc:]
        


def display_grid(grid):
    """Displays the grid. x gets bigger from left to right, y gets bigger from top to bottom"""
    for y in range(len(grid)):
        row = ''
        for x in range(len(grid)):
            if grid[x][y] == 0:
                row += '. '
            else:
                row += str(grid[x][y]) + ' '
        print(row)


def grid_full(grid):
    """Returns True if the grid is full and False if the grid is not full"""
    for x in range(6):
        for y in range(6):
            if grid[x][y] == 0:
                return False
    return True


def make_puzzle():
    """Randomly generates a 6 x 6 sudoku solution."""
    errors = 1
    while errors != 0:
        errors = 0
        grid = gen_grid()
        for x in range(6):
            for y in range(6):
                fill_cell(x, y, grid)
                if grid[x][y] == '@':
                    errors += 1
                    break
            else:                                            # Magic speed boost
                continue
            break

    return grid

