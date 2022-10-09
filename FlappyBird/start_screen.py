import pygame
from settings import Settings

class Start:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.keep_running = True
        self.data = Settings.get_settings()

    def draw(self):
        pass

    def detect_click(self):
        pass

    def play(self):
        print("PLAYING START SCREEN")
        return self.keep_running
