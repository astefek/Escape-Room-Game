import pygame
import sudoku
import maze.mazePuzz
import time
import outro
import shape_puzzle.shape_puzzle as shapes
import simon.simon as simon

pygame.init()
pygame.font.init()

window_width = 720
window_height = 480
window = pygame.display.set_mode([window_width, window_height])

clock = pygame.time.Clock()

def image_load(filename):
    image = pygame.image.load(filename).convert_alpha()
    image = pygame.transform.scale(image, (20, 30))
    return image

def text_print(window, text, size):
    font = pygame.font.SysFont('haettenschweiler', size)
    textsurface = font.render(text, False, (255, 255, 255))
    window.blit(textsurface, ((window_width/2) - (textsurface.get_rect().width/2), (322) - (textsurface.get_rect().height/2)))

def printTime(currentTime):
    mil = currentTime
    totalSec = mil // 1000
    minutes = totalSec // 60
    secs = totalSec % 60 
    return minutes, secs

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

class Robot(pygame.sprite.Sprite):
    """
    stomping robot
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Animation list 
        self.animation = []

        # Index shit
        self.index = 0

        # Loading robot images 
        for _ in range(5):
            self.animation.append(image_load('robo1.png'))
        for _ in range(5):
            self.animation.append(image_load('robo2.png'))
        for _ in range(5):
            self.animation.append(image_load('robo3.png'))
        
        # Rect and pos 
        self.image = self.animation[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (541, 331)
    
    def update(self):
        self.index += 1 
        if self.index >= len(self.animation):
            self.index = 0 
        self.image = self.animation[self.index]

class Floaty(pygame.sprite.Sprite):
    """
    stomping robot
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Animation list 
        self.animation = []

        # Index shit
        self.index = 0

        # Loading robot images 
        for _ in range(10):
            self.animation.append(image_load('floaty1.png'))
        for _ in range(10):
            self.animation.append(image_load('floaty2.png'))
        for _ in range(10):
            self.animation.append(image_load('floaty3.png'))
        for _ in range(10):
            self.animation.append(image_load('floaty4.png'))

        # Rect and pos 
        self.image = self.animation[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (200, 171)
    
    def update(self):
        self.index += 1 
        if self.index >= len(self.animation):
            self.index = 0 
        self.image = self.animation[self.index]

    

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

robo = Robot()
all_sprites.add(robo)

floaty = Floaty()
all_sprites.add(floaty)


def run(window, bg):
    puzzles_solved = 0
    timer = 0
    plant_text = False
    escape_text = False
    robo_text = False
    floaty_text = False
    time_text = False
    


    while True:
        timer += clock.tick(30)
        

        # Drawing
        window.blit(bg, (0,0))
        all_sprites.update()
        all_sprites.draw(window)
        
        # Text Stuff 
        if plant_text == True:
            text_print(window, 'The plant seems alright for now.', 25)
            plant_ev = pygame.event.get()
            for event in plant_ev:
                if event.type == pygame.MOUSEBUTTONUP:
                    plant_text = False

        if escape_text == True:
            text_print(window, "Really? You're gonna try and escape? Wimp.", 20)
            escape_ev = pygame.event.get()
            for event in escape_ev:
                if event.type == pygame.MOUSEBUTTONUP:
                    escape_text = False

        if robo_text == True:
            text_print(window, "Admiral Gears: 'Please put out the fires...'", 20)
            robo_ev = pygame.event.get()
            for event in robo_ev:
                if event.type == pygame.MOUSEBUTTONUP:
                    robo_text = False

        if floaty_text == True:
            text_print(window, "Lt. Bolts: 'Try clicking around the room'", 20)
            floaty_ev = pygame.event.get()
            for event in floaty_ev:
                if event.type == pygame.MOUSEBUTTONUP:
                    floaty_text = False
        """
        if time_text == True:
            currentTime = clock.get_time()
            minutes, secs = printTime(currentTime)
            timing = str(minutes) + ':' + str(secs)
            text_print(window, timing, 50)
            time_ev = pygame.event.get()
            for event in time_ev:
                if event.type == pygame.MOUSEBUTTONUP:
                    time_text = False
            """

            
        # Sprite Clicking
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                pygame.quit()
            #MOUSEBUTTONUP 
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in all_sprites if s.rect.collidepoint(pos)]

                # Decorations
                if clicked_sprites == [tube]:
                    plant_text = True
                if clicked_sprites == [escape]:
                    escape_text = True
                if clicked_sprites == [robo]:
                    robo_text = True
                if clicked_sprites == [floaty]:
                    floaty_text = True
                if clicked_sprites == [panel]:
                    time_text = True

                # Puzzles
                if clicked_sprites == [screen]:
                    puzzles_solved = sudoku.puzzle.run(window, puzzles_solved)
                if clicked_sprites == [maze_panel]:
                    puzzles_solved = maze.mazePuzz.run(window, puzzles_solved)
                if clicked_sprites == [symbol]:
                    puzzles_solved = shapes.run(window, puzzles_solved)
                if clicked_sprites == [simonsays]:
                    puzzles_solved = simon.run(window, puzzles_solved)

        pygame.display.flip()

        if puzzles_solved == 4:
            return 2

        


                



