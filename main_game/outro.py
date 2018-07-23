
import pygame 

import time

import sys

pygame.init()
pygame.font.init()



window_width = 720
window_height = 480
window = pygame.display.set_mode([window_width, window_height])

outro_clock = pygame.time.Clock()
startbg = pygame.image.load('start_screenbg.png').convert()

state = 0

def image_load(filename):
    image = pygame.image.load(filename).convert_alpha()
    image = pygame.transform.scale(image, (20, 30))
    return image


def loop(window):
    global state
    outro_clock.tick(30)
    if state == 0:
        flame_sprite.update()
        flame_sprite.draw(window) 
        if pygame.time.get_ticks() < 3000:  
            state = 0
            return state
        else:
            state = 1
            return state
    if state == 1:
        if pygame.time.get_ticks() < 5000:
            state = 1
            return state
        else:
            state = 2
            return state
    elif state == 2:
        if pygame.time.get_ticks() < 8000:
            text_print(window, 'Hey, good job', 80)
            state = 2
            return state
        else:
            state = 3
            return state
    elif state == 3:
        if pygame.time.get_ticks() < 10000:
            text_print(window, "You didn't blow up", 80)
            state = 3 
            return state
        else:
            state = 4 
            return state
    elif state == 4:
        if pygame.time.get_ticks() < 12000:
            text_print(window, "Try to drive better next time", 50)
            state = 4 
            return state 
        else:
            state = 5
            return state
    else:
        return 

    
def text_print(window, text, size):
    font = pygame.font.SysFont('haettenschweiler', size)
    textsurface = font.render(text, False, (255, 255, 255))
    window.blit(textsurface, ((window_width/2) - (textsurface.get_rect().width/2), (window_height/2) - (textsurface.get_rect().height/2)))


class Flames(pygame.sprite.Sprite):
    """ 
    #Creates moving flames during intro screen
    """
    def __init__(self):
        # Constructor function
        pygame.sprite.Sprite.__init__(self)

        # Flames animation list
        self.animation = []

         # Index shit
        self.index = 0 

        # Loading all flame images 
        self.animation.append(image_load('flame1.png'))
        self.animation.append(image_load('flame2.png'))
        self.animation.append(image_load('flame3.png'))
        self.animation.append(image_load('flame4.png'))
        self.animation.append(image_load('flame5.png'))
        self.animation.append(image_load('flame6.png'))
        self.animation.append(image_load('flame7.png'))

        # Rect and pos
        self.image = self.animation[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (407, 275)
    
    def update(self):

        self.index += 1 
        if self.index >= len(self.animation):
            self.index = 0 
        self.image = self.animation[self.index]

class Flames2(pygame.sprite.Sprite):
    """ 
    #Creates moving flames during intro screen
    """
    def __init__(self):
        # Constructor function
        pygame.sprite.Sprite.__init__(self)

        # Flames animation list
        self.animation = []

         # Index shit
        self.index = 0 

        # Loading all flame images 
        self.animation.append(image_load('flame1.png'))
        self.animation.append(image_load('flame2.png'))
        self.animation.append(image_load('flame3.png'))
        self.animation.append(image_load('flame4.png'))
        self.animation.append(image_load('flame5.png'))
        self.animation.append(image_load('flame6.png'))
        self.animation.append(image_load('flame7.png'))

        # Rect and pos
        self.image = self.animation[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (347, 201)
    
    def update(self):

        self.index += 1 
        if self.index >= len(self.animation):
            self.index = 0 
        self.image = self.animation[self.index]


# Fire shit 
flame_sprite = pygame.sprite.Group()
flames = Flames()
flame_sprite.add(flames)
flames2 = Flames2()
flame_sprite.add(flames2)
flame_sprite.update()


def run(window, bg):
    global state
    window.blit(bg, (0, 0))
    state = loop(window)
    pygame.display.flip()
    if state == 5:
        pygame.QUIT()



