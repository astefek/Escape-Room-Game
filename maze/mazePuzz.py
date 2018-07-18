import mazetest
import pygame

pygame.init()

winWid = 720
winHi = 480
window = pygame.display.set_mode([winWid, winHi])
windowColor = pygame.Color(165, 172, 186)

# a List-of-Lists, composed of boolean elements, detailing the mechanics of the maze
mazeMap = mazetest.maze(width=50, height=50, complexity=0.25, density=0.25)
LoL = list(mazeMap)

# +++ DRAWING THE MAZE W/ END GOAL+++ #

def neighborCount(grid, c, r):
    """
    Counts the number of open spaces for each cell in the maze
    """
    liveCount = 0
    if grid[(c - 1)][(r - 1)] == False: #1 UL
        liveCount += 1
    if grid[c][(r - 1)] == False: #2 UC
        liveCount += 1
    if grid[(c + 1)][(r - 1)] == False: #3 UR
        liveCount += 1
    if grid[(c + 1)][r] == False: #4 CR
        liveCount+= 1
    if grid[(c + 1)][(r + 1)] == False: #5 LR
        liveCount == 1
    if grid[c][(r + 1)] == False: #6 LC
        liveCount += 1
    if grid[(c - 1)][(r + 1)] == False: #7 LL
        liveCount += 1
    if grid[(c - 1)][r] == False: #8 CL
        liveCount += 1
    return liveCount

def findEnd(mazeMap):
    """
    From the bottom right, scans the maze for any rooms (defined by False neighbors)
    then places the end point at the first possible room
    """
    LoL = list(mazeMap)
    for r in range(len(LoL)-1, 0, -1):
        for c in range(len(LoL[r]) -1, 0, -1):
            if LoL[r][c] == False:
                liveCount = neighborCount(LoL, c, r)
                if liveCount >= 6:
                    posn = (c, r)
                    return posn

def drawEnd(mazeMap):
    """
    Draws a rect at the endpoint found by findEnd
    """
    scaleFactWid = winWid/len(LoL)
    scaleFactHi = winHi/len(LoL) 
    posn = findEnd(mazeMap)
    for r in range(len(LoL)):
        for c in range(len(LoL[r])):
            if (c, r) == posn:
                pygame.draw.rect(window, (88, 189, 81), (c * scaleFactWid, r * scaleFactHi, scaleFactWid, scaleFactHi))

def drawMaze(mazeMap):
    """
    Converts the [list-of-lists] created through mazetest into a pygame display
    """
    scaleFactWid = winWid/len(LoL)
    scaleFactHi = winHi/len(LoL) 
    for r in range(len(LoL)):
        for c in range(len(LoL[r])):
            if LoL[r][c] == True:
                pygame.draw.rect(window, (64, 70, 83), (c * scaleFactWid, r * scaleFactHi, scaleFactWid, scaleFactHi))
    drawEnd(mazeMap)

# +++ MAKING THE PLAYER ITEM +++ #
scaleFactWid = winWid/len(LoL)
scaleFactHi = winHi/len(LoL)
playerSurface = window 
playerColor = pygame.Color(217, 226, 115) 
playerSize = (scaleFactWid, scaleFactHi)
playerPosn = (scaleFactWid, scaleFactHi)

## VERIFY WALLS WIP###
def verifyMove():
    """
    Recieves a 


    Returns True if a move is valid, False otherwise (moving into a wall)
    """


# +++ PLAYING THE GAME +++ #             
while True:
    window.fill(windowColor)
    drawMaze(LoL)
    pygame.draw.rect(playerSurface, playerColor, (playerPosn, playerSize))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerPosn = (playerPosn[0], playerPosn[1] - scaleFactHi)
            if event.key == pygame.K_DOWN:
                playerPosn = (playerPosn[0], playerPosn[1] + scaleFactHi)
            if event.key == pygame.K_LEFT:
                playerPosn = (playerPosn[0] - scaleFactWid, playerPosn[1])
            if event.key == pygame.K_RIGHT:
                playerPosn = (playerPosn[0] + scaleFactWid, playerPosn[1])
        pygame.display.flip()