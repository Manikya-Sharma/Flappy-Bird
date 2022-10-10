import pygame
from flappy import Flappy
from images import Images
from settings import Settings

class Level:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.data = Settings.get_settings()
        self.image_provider = Images()
        self.bg_img = self.image_provider.get_bg_images()[self.data["TIME"]]
        self.flappy = Flappy(20, 200)

    def blit(self):
        # back ground
        self.screen.blit(self.bg_img, (0,0))

    def play(self, dt):
        self.blit()
        self.flappy.play(dt)
        return True   # End
