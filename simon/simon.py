import pygame
import random
import time


# ++++ SETTING PARAMETERS ++++ #

# making the window #

winWid = 720
winHi = 480
window = pygame.display.set_mode([winWid, winHi])


windowSurface = pygame.Surface((winWid, winHi))

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
        # [NOPE] change self.image to -> pygame.draw.rect(window, LIGHTBLUE, self.rect) when lit

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
        # [NOPE] change self.image to -> pygame.draw.rect(window, LIGHTRED, self.rect) when lit

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
        # [NOPE] change self.image to -> pygame.draw.rect(window, LIGHTGREEN, self.rect) when lit

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
        # [NOPE] change self.image to -> pygame.draw.rect(window, LIGHTYELLOW, self.rect) when lit

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

# ++++ CREATING THE BACK-END ++++ #
# features two phases of play -- the read phase and the input phase

def buildList(gameList):
    """
    Builds the list of buttons fit for a simon says game.

    On each call, adds a random element to the constructed list.
    Previous elements remain unchanged.
    """
    #gameList += [random.choice(['b', 'r', 'g', 'y'])]
    gameList.append(random.choice(['b', 'r', 'g', 'y']))
    #return gameList

def readList(gameList):
    """
    Takes in a gameList and flashes the button for each corrosponding
    element in the gameList
    """

    for color in gameList:
        if color == 'b':
            pygame.draw.rect(window, LIGHTBLUE, blueButton.rect)
            pygame.display.flip()
            time.sleep(0.5)
            pygame.draw.rect(window, BLUE, blueButton.rect)
            pygame.display.flip()
        elif color == 'r':
            pygame.draw.rect(window, LIGHTRED, redButton.rect)
            pygame.display.flip()
            time.sleep(0.5)
            pygame.draw.rect(window, RED, redButton.rect)
            pygame.display.flip()
        elif color == 'g':
            pygame.draw.rect(window, LIGHTGREEN, greenButton.rect)
            pygame.display.flip()
            time.sleep(0.5)
            pygame.draw.rect(window, GREEN, greenButton.rect)
            pygame.display.flip()
        elif color == 'y':
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

def seeInput():
    """
    On a click, flashes the selected button and returns it as input
    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if blueButton.rect.collidepoint(event.pos):
                    pygame.draw.rect(window, LIGHTBLUE, blueButton.rect)
                    pygame.display.flip()
                    return 'b'
                elif redButton.rect.collidepoint(event.pos):
                    pygame.draw.rect(window, LIGHTRED, redButton.rect)
                    pygame.display.flip()
                    return 'r'
                elif greenButton.rect.collidepoint(event.pos):
                    pygame.draw.rect(window, LIGHTGREEN, greenButton.rect)
                    pygame.display.flip()
                    return 'g'
                elif yellowButton.rect.collidepoint(event.pos):
                    pygame.draw.rect(window, LIGHTYELLOW, yellowButton.rect)
                    pygame.display.flip()
                    return 'y'
            elif event.type == pygame.QUIT:
                pygame.quit()
            
    
# def checkMove(answer, input):
#     """
#     Checks each input to see if it aligns with each element in
#     the gameList
#     """
#     return input == answer
#         #buildList(gameList)

#     # for color in gameList:
#     #     #if input == None:
#     #     #    pass
#     #     if input != color:
#     #         gameList = []
#     #         return gameList
#     # return gameList

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

def checkWin(gameList, puzzleSolved):
    """
    Checks to see if the player has won
    """
    if len(gameList) >= 8:
        puzzleSolved += 1
        print("a winner is you!")

# +*~*+ RUNNING THE GAME +*~*+ #
def run(window, puzzleSolved, gameList=[]):
    while True:
        playRound(gameList)
        checkWin(gameList, puzzleSolved)

run(window, 0, [])