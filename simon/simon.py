import pygame
import random
import time


# ++++ SETTING PARAMETERS ++++ #

# making the window #

winWid = 720
winHi = 480
window = pygame.display.set_mode([winWid, winHi])
windowColor = pygame.Color(77, 98, 118)
windowSurface = pygame.Surface((winWid, winHi))
window.fill(windowColor)

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




# +*~*+ RUNNING THE GAME +*~*+ #

while True:
    allButtons.update()
    allButtons.draw(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # on input phase ONLY #
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if blueButton.rect.collidepoint(pos):
                pygame.draw.rect(window, LIGHTBLUE, blueButton.rect)
                pygame.display.flip()
                time.sleep(1)
            elif redButton.rect.collidepoint(pos):
                pygame.draw.rect(window, LIGHTRED, redButton.rect)
                pygame.display.flip()
                time.sleep(1)
            elif greenButton.rect.collidepoint(pos):
                pygame.draw.rect(window, LIGHTGREEN, greenButton.rect)
                pygame.display.flip()
                time.sleep(1)
            elif yellowButton.rect.collidepoint(pos):
                pygame.draw.rect(window, LIGHTYELLOW, yellowButton.rect)
                pygame.display.flip()
                time.sleep(1)

    pygame.display.flip()
