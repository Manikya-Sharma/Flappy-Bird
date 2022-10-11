import pygame


class Timer:
    def __init__(self):
        self.init_ticks = pygame.time.get_ticks()

    def time_elapsed(self):
        return (pygame.time.get_ticks()-self.init_ticks)/1000

    def restart(self):
        self.init_ticks = pygame.time.get_ticks()
