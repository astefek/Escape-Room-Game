import mazetest
import pygame

pygame.init()

# +++ BUILDING THE WINDOW SCENE +++ #
winWid = 720
winHi = 480
window = pygame.display.set_mode([winWid, winHi])
windowColor = pygame.Color(165, 172, 186)


# Variables detailing the inner mechanics of the maze, and its scaling
mazeMap = mazetest.maze(width=50, height=50, complexity=0.9, density=0.9)
LoL = list(mazeMap)
scaleFactWid = winWid/len(LoL)
scaleFactHi = winHi/len(LoL)

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
                if liveCount >= 4:
                    endPosn = (c * scaleFactWid, r * scaleFactHi)
                    return endPosn

def drawEnd(mazeMap):
    """
    Draws a rect at the endpoint found by findEnd
    """
    scaleFactWid = winWid/len(LoL)
    scaleFactHi = winHi/len(LoL) 
    posn = findEnd(mazeMap)
    for r in range(len(LoL)):
        for c in range(len(LoL[r])):
            if (c * scaleFactWid, r * scaleFactHi) == posn:
                endBlock = pygame.draw.rect(window, (88, 189, 81), (c * scaleFactWid, r * scaleFactHi, scaleFactWid, scaleFactHi))
                return endBlock

def makeWall(mazeMap):
    """
    Takes a [list-of-lists] detailing the maze backend and 
    creates a list of Rect objects to be used in collision checks within pygame
    """
    scaleFactWid = winWid/len(LoL)
    scaleFactHi = winHi/len(LoL)
    mazeWallList = []
    for r in range(len(LoL)):
        for c in range(len(LoL[r])):
            if LoL[r][c] == True:
                mazeWall = pygame.Rect(c * scaleFactWid, r * scaleFactHi, scaleFactWid, scaleFactHi)
                mazeWallList += [mazeWall]
    return mazeWallList

def drawMaze(mazeMap):
    """
    Converts the [list-of-lists] created through mazetest into a pygame display
    """
    scaleFactWid = winWid/len(LoL)
    scaleFactHi = winHi/len(LoL)
    mazeWallList = []
    for r in range(len(LoL)):
        for c in range(len(LoL[r])):
            if LoL[r][c] == True:
                mazeWall = (c * scaleFactWid, r * scaleFactHi, scaleFactWid, scaleFactHi)
                pygame.draw.rect(window, (64, 70, 83), mazeWall)
                mazeWallList += mazeWall
    return mazeWallList


# +++ MAKING THE PLAYER ITEM +++ #
playerSurface = window 
playerColor = pygame.Color(217, 226, 115) 
playerSize = (scaleFactWid, scaleFactHi)
playerPosn = (scaleFactWid, scaleFactHi)

# +++ MAKING THE WIN CONDITION +++ #

def solveMaze(playerPosn, endPosn):
    """
    Determines if the player has reached the end Rect of the maze.
    """
    playerPosnX = int(playerPosn[0])
    playerPosnY = int(playerPosn[1])
    playerPosn = (playerPosnX, playerPosnY)
    endPosnX = int(endPosn[0])
    endPosnY = int(endPosn[1])
    endPosn = (endPosnX, endPosnY)
    if playerPosn == endPosn:
        return True
    else:
        return False



# +++ PLAYING THE GAME +++ #             
def run(window, puzzles_solved):
    while True:
        window.fill(windowColor)
        mazeWall = drawMaze(LoL)
        collideableWall = makeWall(LoL)
        mazeEnd = drawEnd(LoL)
        playerRect = pygame.draw.rect(playerSurface, playerColor, (playerPosn, playerSize))
        
        #   On a directional keypress, checks the space ahead,
        # determines if it collides, and if it doesn't, moves the player
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    futurePlayerRect = pygame.Rect(playerPosn[0], playerPosn[1] - scaleFactHi, scaleFactWid, scaleFactHi)
                    if futurePlayerRect.collidelist(collideableWall) == -1:
                        playerPosn = (playerPosn[0], playerPosn[1] - scaleFactHi)
                    
                if event.key == pygame.K_DOWN:
                    futurePlayerRect = pygame.Rect(playerPosn[0], playerPosn[1] + scaleFactHi, scaleFactWid, scaleFactHi)
                    if futurePlayerRect.collidelist(collideableWall) == -1:
                        playerPosn = (playerPosn[0], playerPosn[1] + scaleFactHi)

                if event.key == pygame.K_LEFT:
                    futurePlayerRect = futureUpPlayerRect = pygame.Rect(playerPosn[0] - scaleFactWid, playerPosn[1], scaleFactWid, scaleFactHi)
                    if futurePlayerRect.collidelist(collideableWall) == -1:
                        playerPosn = (playerPosn[0] - scaleFactWid, playerPosn[1])

                if event.key == pygame.K_RIGHT:
                    futurePlayerRect = pygame.Rect(playerPosn[0] + scaleFactWid, playerPosn[1], scaleFactWid, scaleFactHi)
                    if futurePlayerRect.collidelist(collideableWall) == -1:
                        playerPosn = (playerPosn[0] + scaleFactWid, playerPosn[1])
        
        if solveMaze(playerPosn, findEnd(LoL)) == True:
            return puzzles_solved += 1
        
        pygame.display.flip()
    