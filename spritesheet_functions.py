import pygame
pygame.init()

class SpriteSheet(object):
    """
    Used to grab individual sprites from sprite sheet
    """
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()
    
    def get_image(self, x, y, width, height):
        """
        Grab single image from sprite sheet 
        """
        # Create new blank image
        image = pygame.Surface([width, height]).convert()
        
        # copy sprite from large sheet to small image 
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        return image
