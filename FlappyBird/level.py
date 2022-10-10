import pygame
from images import Images
from settings import Settings

class Level:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.data = Settings.get_settings()
        self.image_provider = Images()
        self.bg_img = self.image_provider.get_bg_images()[self.data["TIME"]]

    def blit(self):
        # back ground
        self.screen.blit(self.bg_img, (0,0))


    def play(self):
        self.blit()
        return True   # End
