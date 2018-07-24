
import pygame 

import time

import sys

pygame.init()
pygame.font.init()



window_width = 720
window_height = 480
window = pygame.display.set_mode([window_width, window_height])


startbg = pygame.image.load('start_screenbg.png').convert()

clock = pygame.time.Clock()


def image_load(filename):
    image = pygame.image.load(filename).convert_alpha()
    image = pygame.transform.scale(image, (20, 30))
    return image


def loop(window, cycles, state):
    if state == 0:
        window.blit(startbg, (0,0))
        flame_sprite.update()
        flame_sprite.draw(window)
        if cycles < 1500:  
            state = 0
        else:
            state = 1
    if state == 1:
        if cycles < 2500:
            window.blit(startbg, (0, 0))
            state = 1
        else:
            state = 2
    elif state == 2:
        window.blit(startbg, (0, 0))
        if cycles < 3500:
            text_print(window, 'Hey, good job', 80)
            state = 2
        else:
            state = 3
    elif state == 3:
        window.blit(startbg, (0, 0))
        if cycles < 4500:
            text_print(window, "You didn't blow up", 80)
            state = 3 
        else:
            state = 4 
    elif state == 4:
        window.blit(startbg, (0, 0))
        if cycles < 5500:
            text_print(window, "Try to drive better next time", 50)
            state = 4 
        else:
            state = 5
    cycles += 1
    return state, cycles
    
    

    
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
    state = 0
    window.blit(bg, (0, 0))
    
    cycles = 0 

    while state < 5:
        state, cycles = loop(window, cycles, state)
        pygame.display.flip()
    if state == 5:
        pygame.quit()


