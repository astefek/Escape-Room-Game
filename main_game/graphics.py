import pygame
import sudoku
import maze.mazePuzz
import time
import outro


pygame.init()
pygame.font.init()

window_width = 720
window_height = 480
window = pygame.display.set_mode([window_width, window_height])

def text_print(window, text, size):
    font = pygame.font.SysFont('arial', size)
    textsurface = font.render(text, False, (255, 255, 255))
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

class EscapePod(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('escapepod.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (193, 278)

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

escape = EscapePod()
all_sprites.add(escape)


def run(window, bg):
    puzzles_solved = 0
    plant_text = False
    escape_text = False

    while True:
        window.blit(bg, (0,0))
        all_sprites.update()
        all_sprites.draw(window)
        
        if plant_text == True:
            text_print(window, 'The plant seems alright for now.', 25)
            plant_ev = pygame.event.get()
            for event in plant_ev:
                if event.type == pygame.MOUSEBUTTONUP:
                    plant_text = False

        if escape_text == True:
            text_print(window, "Really? You're gonna try and escape? Wimp.", 15)
            escape_ev = pygame.event.get()
            for event in escape_ev:
                if event.type == pygame.MOUSEBUTTONUP:
                    escape_text = False

        ev = pygame.event.get()
        for event in ev:
            #MOUSEBUTTONUP 
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in all_sprites if s.rect.collidepoint(pos)]
                if clicked_sprites == [tube]:
                    plant_text = True
                if clicked_sprites == [escape]:
                    escape_text = True
                if clicked_sprites == [screen]:
                    puzzles_solved = sudoku.puzzle.run(window, puzzles_solved)
                if clicked_sprites == [maze_panel]:
                    puzzles_solved = maze.mazePuzz.run(window, puzzles_solved)
        pygame.display.flip()


                



