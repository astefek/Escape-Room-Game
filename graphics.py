import pygame

pygame.init()

# Window/background details 
window_width = 720
window_height = 480
window = pygame.display.set_mode([window_width, window_height])

bg = pygame.image.load('space_gamebg.png').convert()

window.blit(bg, (0,0))

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
        self.rect.center = (330, 120)

class Screen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('screen.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (235, 200)

class Maze_panel(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('maze_panel.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (370, 270)


panel = Panel()
all_sprites.add(panel)

screen = Screen()
all_sprites.add(screen)

maze_panel = Maze_panel()
all_sprites.add(maze_panel)

all_sprites.update()
all_sprites.draw(window)



pygame.display.flip()

while True:
    pass
   
    





