
import pygame 

import time

import sys


pygame.init()

clock = pygame.time.Clock()

window_width = 720
window_height = 480
window = pygame.display.set_mode([window_width, window_height])

startbg = pygame.image.load('start_screenbg.png').convert()
window.blit(startbg, (0,0))

# Font shit
pygame.font.init()
font = pygame.font.SysFont('haettenschweiler', 90)


def image_load(filename):
    image = pygame.image.load(filename).convert_alpha()
    image = pygame.transform.scale(image, (20, 30))
    return image


def loop(state):
    clock.tick(30)
    if state == 0:
        asteroid_sprite.update()
        asteroid_sprite.draw(window)
        if pygame.time.get_ticks() < 6000:
            state = 0
            return state
        else:
            state = 1
            return state
    elif state == 1:
        flame_sprite.update()
        flame_sprite.draw(window)
        if pygame.time.get_ticks() < 9000:
            state = 1
            return state
        else:
            state = 2
            return state
    elif state == 2:
        flame_sprite.update()
        flame_sprite.draw(window)
        if pygame.time.get_ticks() < 12000:
            text_print('WARNING', 90)
            state = 2 
            return state
        else:
            state = 3 
            return state
    elif state == 3:
        flame_sprite.update()
        flame_sprite.draw(window)
        if pygame.time.get_ticks() < 19000:
            text_print('FIX ENGINE OR FACE CERTAIN DOOM', 50)
            state = 3 
            return state 
        else:
            state = 4
            return state
    
        
def text_print(text, size):
    pygame.font.init()
    font = pygame.font.SysFont('haettenschweiler', size)
    textsurface = font.render(text, False, (255, 0, 25))
    window.blit(textsurface, ((window_width/2) - (textsurface.get_rect().width/2), (window_height/2) - (textsurface.get_rect().height/2)))

class Asteroid(pygame.sprite.Sprite):
    """
    #Creates the moving asteroid
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('asteroid.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (705, 11)

    def update(self):
        self.rect.x += (-5)
        self.rect.y += 2


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

# Asteroid shit 
asteroid_sprite = pygame.sprite.Group()
asteroid = Asteroid()
asteroid_sprite.add(asteroid)


# Fire shit 
flame_sprite = pygame.sprite.Group()

flames = Flames()
flame_sprite.add(flames)

flames2 = Flames2()
flame_sprite.add(flames2)


state = 0
while True:
    window.blit(startbg, (0, 0))
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)
    
    state = loop(state)
        

    pygame.display.flip()

