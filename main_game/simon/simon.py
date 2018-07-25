import pygame
import random
import time

pygame.init()
pygame.mixer.init()

# ++++ SETTING PARAMETERS ++++ #

# Escape definition
escape = False

# making the window #

winWid = 720
winHi = 480
window = pygame.display.set_mode([winWid, winHi])

# making the board #
border = 10
dubBorder = 2 * border

# colors! #
BLUE = (58, 58, 191)
LIGHTBLUE = (107, 120, 203)

RED = (127, 50, 46)
LIGHTRED = (166, 68, 97)

GREEN = (36, 134, 23)
LIGHTGREEN = (85, 255, 66)

YELLOW = (201, 171, 75)
LIGHTYELLOW = (220, 198, 131)

defaultWindowColor = pygame.Color(77, 98, 118)
READPHASECOLOR = (152, 38, 73)
INPUTPHASECOLOR = (127, 183, 190)

# sounds! #

blueSound = pygame.mixer.Sound("A4.wav")
redSound = pygame.mixer.Sound("B4.wav")
greenSound = pygame.mixer.Sound("D5.wav")
yellowSound = pygame.mixer.Sound("E5.wav")

# mouse/cursor #
pygame.mouse.set_cursor(*pygame.cursors.arrow)

# sprites #
allButtons = pygame.sprite.Group()

class blueButton(pygame.sprite.Sprite):
    #constructor below
    def __init__(self):
        # parent constructor 
        pygame.sprite.Sprite.__init__(self)
        # button hitbox/rect
        self.rect = pygame.Rect((border, border), ((winWid / 2)- dubBorder, (winHi / 2) - dubBorder))
        # button image display
        self.image = pygame.Surface([(winWid / 2)- dubBorder, (winHi / 2) - dubBorder])
        self.image.fill(BLUE)

class redButton(pygame.sprite.Sprite):
    #constructor below
    def __init__(self):
        # parent constructor 
        pygame.sprite.Sprite.__init__(self)
        # button hitbox/rect
        self.rect = pygame.Rect(((winWid / 2) + border, border), ((winWid / 2)- dubBorder, (winHi / 2) - dubBorder))
        # button image display
        self.image = pygame.Surface([(winWid / 2)- dubBorder, (winHi / 2) - dubBorder])
        self.image.fill(RED)

class greenButton(pygame.sprite.Sprite):
    #constructor below
    def __init__(self):
        # parent constructor 
        pygame.sprite.Sprite.__init__(self)
        # button hitbox/rect
        self.rect = pygame.Rect((border, (winHi / 2) + border), ((winWid / 2)- dubBorder, (winHi / 2) - dubBorder))
        # button image display
        self.image = pygame.Surface([(winWid / 2)- dubBorder, (winHi / 2) - dubBorder])
        self.image.fill(GREEN)

class yellowButton(pygame.sprite.Sprite):
    #constructor below
    def __init__(self):
        # parent constructor 
        pygame.sprite.Sprite.__init__(self)
        # button hitbox/rect
        self.rect = pygame.Rect(((winWid / 2) + border, (winHi / 2) + border), ((winWid / 2)- dubBorder, (winHi / 2) - dubBorder))
        # button image display
        self.image = pygame.Surface([(winWid / 2)- dubBorder, (winHi / 2) - dubBorder])
        self.image.fill(YELLOW)

# ++++ CONSTRUCTING SPRITES ++++ #

blueButton = blueButton()
allButtons.add(blueButton)

redButton = redButton()
allButtons.add(redButton)

greenButton = greenButton()
allButtons.add(greenButton)

yellowButton = yellowButton()
allButtons.add(yellowButton)

# ++++ ESTABLISHING PHASE BG ++++ #

def changeBG(color):
    """
    Takes a color and changes the background to be that color
    """
    window.fill(color)
    allButtons.draw(window)
    pygame.display.flip()

# +-*-+ CREATING THE BACK-END +-*-+ #
# features two phases of play -- the read phase and the input phase


# ++++ READ PHASE ++++ #
def buildList(gameList):
    """
    Builds the list of buttons fit for a simon says game.

    On each call, adds a random element to the constructed list.
    Previous elements remain unchanged.
    """
    gameList.append(random.choice(['b', 'r', 'g', 'y']))

def readList(gameList):
    """
    Takes in a gameList and flashes the button for each corrosponding
    element in the gameList
    """

    for color in gameList:
        if color == 'b':
            blueSound.play()
            pygame.draw.rect(window, LIGHTBLUE, blueButton.rect)
            pygame.display.flip()
            time.sleep(0.5)
            pygame.draw.rect(window, BLUE, blueButton.rect)
            pygame.display.flip()
        elif color == 'r':
            redSound.play()
            pygame.draw.rect(window, LIGHTRED, redButton.rect)
            pygame.display.flip()
            time.sleep(0.5)
            pygame.draw.rect(window, RED, redButton.rect)
            pygame.display.flip()
        elif color == 'g':
            greenSound.play()
            pygame.draw.rect(window, LIGHTGREEN, greenButton.rect)
            pygame.display.flip()
            time.sleep(0.5)
            pygame.draw.rect(window, GREEN, greenButton.rect)
            pygame.display.flip()
        elif color == 'y':
            yellowSound.play()
            pygame.draw.rect(window, LIGHTYELLOW, yellowButton.rect)
            pygame.display.flip()
            time.sleep(0.5)
            pygame.draw.rect(window, YELLOW, yellowButton.rect)
            pygame.display.flip()
        time.sleep(1)
    pygame.event.clear()
    return gameList


def readPhase(gameList):
    """
    Builds a gameList, then displays it to the user
    """
    buildList(gameList)
    time.sleep(1)
    readList(gameList)


# ++++ INPUT PHASE ++++ #

def seeInput():
    global escape
    """
    On a click, flashes the selected button and returns it as input
    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if blueButton.rect.collidepoint(event.pos):
                    blueSound.play()
                    pygame.draw.rect(window, LIGHTBLUE, blueButton.rect)
                    pygame.display.flip()
                    return 'b'
                elif redButton.rect.collidepoint(event.pos):
                    redSound.play()
                    pygame.draw.rect(window, LIGHTRED, redButton.rect)
                    pygame.display.flip()
                    return 'r'
                elif greenButton.rect.collidepoint(event.pos):
                    greenSound.play()
                    pygame.draw.rect(window, LIGHTGREEN, greenButton.rect)
                    pygame.display.flip()
                    return 'g'
                elif yellowButton.rect.collidepoint(event.pos):
                    yellowSound.play()
                    pygame.draw.rect(window, LIGHTYELLOW, yellowButton.rect)
                    pygame.display.flip()
                    return 'y'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    escape = True
                    return
            elif event.type == pygame.QUIT:
                pygame.quit()
            


def inputPhase(gameList):
    """
    Determines the user's input and checks to see if it matches
    the gameList
    """

    next = 0
    while True:
        if gameList[next] == seeInput():
            next += 1
            time.sleep(0.5)
            allButtons.draw(window)
            pygame.display.flip()
        else:
            gameList.clear()
            time.sleep(0.5)
            allButtons.draw(window)
            pygame.display.flip()
            break
        if next >= len(gameList):
            break



def playRound(gameList):
    """
    Runs a turn of simon-says, or cycles through the two phases in the game
    """
    changeBG(READPHASECOLOR)
    readPhase(gameList)
    changeBG(INPUTPHASECOLOR)
    inputPhase(gameList)

def checkWin(gameList):
    """
    Checks to see if the player has won
    """
    if len(gameList) == 8:
        return True


# +*~*+ RUNNING THE GAME +*~*+ #
def run(window, gameList=[]):
    global escape
    """
    Runs the game.

    The run function subsists on 2 functions,
    one to play a single round, and one to 
    check to see if the player has won the whole game. 
    """
    while True:
        escape = False
        playRound(gameList)
        if checkWin(gameList) == True:
            return True
        if escape:
            gameList = []
            return False
        

