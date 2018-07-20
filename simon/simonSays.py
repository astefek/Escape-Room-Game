import pygame
import math
import random

pygame.init()

# CHECKLIST #
#   1. draw the shapes
#   2. make the shapes glow when called
#   3. change input method (maybe a new function?)
#   4. add timer

# +++ BUILDING THE WINDOW SCENE +++ #
winWid = 720
winHi = 480
window = pygame.display.set_mode([winWid, winHi])
windowColor = pygame.Color(77, 98, 118)

# +++ GAME MECHANICS +++ #

def buildList(gameList):
    """
    Defines the sequence for Simon Says through a list.
    Selects a random color choice, and adds it to the list
    """
    gameList += [random.choice(['b', 'r', 'g', 'y'])]
    print(gameList)
    gameTurn(gameList)

def gameTurn(gameList):
    """
    Gathers the user input and references it with each index of buildList
    If it's right, moves on to the next index
    If it's wrong, converts gameList into an [empty List]
    """
    for color in gameList:
        userInput = input("Choice: ") # Will change for pygame
        if userInput != color:
            return buildList([])
    if isWinningList(gameList):
        print("winner is u") 
        return True
    else:
        return gameList + buildList(gameList)

def isWinningList(gameList):
    """
    Counts the gameList.
    If the player gets an 8-element list correct,
    the game is won.
    """
    if len(gameList) == 8:
        return True
    else:
        return False

# +++ DRAWING THE FRONT-END +++ #

BLUE = (58, 58, 191)
RED = (127, 50, 46)
GREEN = (85, 255, 66)
YELLOW = (201, 171, 75)

class Button(pygame.sprite.Sprite):
    """
    Defines the button class of sprite.
    """
    def __init__(self, color, left, top, wid, hi):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([wid, hi])
        self.image.fill(color)

        self.rect = (left, top, wid, hi)

border = 10
twoborder = 2*border
bButton = Button(BLUE, border, border, 360 - twoborder, 240 - twoborder)
rButton = Button(RED, (winWid/2)+border, border, 360 - twoborder, 240 - twoborder)
gButton = Button(GREEN, border, (winHi/2)+border, 360 - twoborder, 240 - twoborder)
yButton = Button(YELLOW, (winWid/2)+border, (winHi/2)+border, 360 - twoborder, 240 - twoborder)
bButtonImage = pygame.draw.rect(window, BLUE, bButton.rect)
rButtonImage = pygame.draw.rect(window, RED, rButton.rect)
gButtonImage = pygame.draw.rect(window, GREEN, gButton.rect)
yButtonImage = pygame.draw.rect(window, YELLOW, yButton.rect)

def drawButtons(bButtonImage, rButtonImage, gButtonImage, yButtonImage):
    """
    Draws each button
    """
    bButtonImage = pygame.draw.rect(window, BLUE, bButton.rect)
    rButtonImage = pygame.draw.rect(window, RED, rButton.rect)
    gButtonImage = pygame.draw.rect(window, GREEN, gButton.rect)
    yButtonImage = pygame.draw.rect(window, YELLOW, yButton.rect)

### Optimize above? We'll see how the glow effect goes (draw another larger rect behind the glowing one????)

# +++ RUNNING THE PUZZLE +++ #
while True:
    window.fill(windowColor)
    drawButtons(bButtonImage, rButtonImage, gButtonImage, yButtonImage)
    pygame.display.flip()

    
