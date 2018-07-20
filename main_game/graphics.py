import pygame

pygame.init()

# Window/background details 
window_width = 720
window_height = 480
window = pygame.display.set_mode([window_width, window_height])

bg = pygame.image.load('space_gamebg.png').convert()

window.blit(bg, (0,0))

# Mouse/Cursor 
pygame.mouse.set_cursor(*pygame.cursors.arrow)

def text_print(text, size):
    pygame.font.init()
    font = pygame.font.SysFont('Arial', size)
    textsurface = font.render(text, False, (255, 0, 25))
    window.blit(textsurface, ((window_width/2) - (textsurface.get_rect().width/2), (window_height/2) - (textsurface.get_rect().height/2)))


# Sprites 
all_sprites = pygame.sprite.Group()

class Panel(pygame.sprite.Sprite):
    # Constructor 
    def __init__(self):
        # Parent constructor 
        pygame.sprite.Sprite.__init__(self)
        # Image of sprite   
        self.image = pygame.image.load('control_panel.png').convert_alpha()
        # Update position 
        self.rect = self.image.get_rect()
        self.rect.center = (368, 120)

class Screen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('screen.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (240, 76)

class Maze_panel(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('maze_panel.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (370, 270)

class Symbol_panel(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('symbol_panel.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (530, 246)

class Tube(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('tube.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (194, 410)

class SimonSays(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('simonsays.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (532, 436)

# Adding Sprites 
panel = Panel()
all_sprites.add(panel)

screen = Screen()
all_sprites.add(screen)

maze_panel = Maze_panel()
all_sprites.add(maze_panel)

symbol = Symbol_panel()
all_sprites.add(symbol)

tube = Tube()
all_sprites.add(tube)

simonsays = SimonSays()
all_sprites.add(simonsays)

all_sprites.update()
all_sprites.draw(window)

def run(window):
    while True:
    pygame.display.flip()
    ev = pygame.event.get()
    for event in ev:
        #MOUSEBUTTONUP 
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in all_sprites if s.rect.collidepoint(pos)]
            if clicked_sprites = [tube]:
                text_print('The plant seems alright for now.', 40)
            if clicked_sprites = [screen]:
                


