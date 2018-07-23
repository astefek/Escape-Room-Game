import pygame
import sudoku
import maze.mazePuzz


pygame.init()
pygame.font.init()

window_width = 720
window_height = 480
window = pygame.display.set_mode([window_width, window_height])

def text_print(window, text, size):
    font = pygame.font.SysFont('arial', size)
    textsurface = font.render(text, False, (0, 0, 0))
    print(textsurface)
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


def run(window, bg):
    puzzles_solved = 0
    plant_text = False

    while True:
        window.blit(bg, (0,0))
        all_sprites.update()
        all_sprites.draw(window)
        
        if plant_text == True:
            text_print(window, 'The plant seems alright for now.', 60)
            new_clock = pygame.time.Clock.tick()
            if plant_clock == new_clock + 5000:
                plant_text = False

        ev = pygame.event.get()
        for event in ev:
            #MOUSEBUTTONUP 
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in all_sprites if s.rect.collidepoint(pos)]
                if clicked_sprites == [tube]:
                    plant_text = True
                    plant_clock = pygame.time.Clock.tick()
                if clicked_sprites == [screen]:
                    puzzles_solved = sudoku.puzzle.run(window, puzzles_solved)
                if clicked_sprites == [maze_panel]:
                    puzzles_solved = maze.mazePuzz.run(window, puzzles_solved)
        pygame.display.flip()
                



