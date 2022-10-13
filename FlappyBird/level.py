import pygame
from flappy import Flappy
from pillar import Pillar
from images import Images
from settings import Settings

class Bg_Images:
    def __init__(self, img_1, img_2, pos_x_1, screen_width, flappy_bound):
        self.img_1 = img_1
        self.img_2 = img_2
        self.pos_x_1 = pos_x_1
        self.screen_width =screen_width
        self.pos_x_2 = self.pos_x_1+self.img_1.get_width()
        self.flappy_bound = flappy_bound
        self.speed = self.flappy_bound.x_speed

    def draw(self, screen):
        screen.blit(self.img_1, (self.pos_x_1,0))
        screen.blit(self.img_2, (self.pos_x_2,0))

    def move(self, dt):
        if self.pos_x_1+self.img_1.get_width() < 0:
            self.pos_x_1 = self.screen_width
        elif self.pos_x_2+self.img_1.get_width() < 0:
            self.pos_x_2 = self.screen_width
        self.pos_x_1 -= self.speed*dt
        self.pos_x_2 -= self.speed*dt

class Level:
    def __init__(self):
        # Initialize
        self.screen = pygame.display.get_surface()
        self.data = Settings.get_settings()
        # Flappy
        self.flappy = Flappy(self.screen.get_size()[0]*(1/10), self.screen.get_height()/2)
        # Background image
        self.image_provider = Images()
        bg_img_1 = self.image_provider.get_bg_images()[self.data["TIME"]]
        bg_img_2 = self.image_provider.get_bg_images()[self.data["TIME"]]
        self.handle_bg = Bg_Images(bg_img_1, bg_img_2, 0, self.screen.get_size()[0],
         self.flappy)
        # Pillars
        Pillar(self.flappy)
        # Score
        self.score = 0
        self.num_images = self.image_provider.get_number_images()

        # Start Game TODO only after play button
        self.flappy.start_moving()

    def blit(self):
        # background
        self.handle_bg.draw(self.screen)
        for letter in str(self.score):
            self.screen.blit(self.num_images.get(letter), (0,0))

    def update_score(self):
        i = 0
        for max_x in Pillar.pillars_max_list:
            if (self.flappy.pos_x >= max_x):
                i += 1
        self.score = i


    def update(self):
        Pillar.update_pillars_creation\
            (self.flappy, self.screen.get_size()[0]*(1/5), self.screen.get_size()[0])
        if Pillar.check_collisions():
            self.flappy.die()

        self.update_score()

    def play(self, dt):
        # Update:-
        self.update()
        self.blit()
        # Pillars:-
        for pillar in Pillar.pillars_list:
            pillar.play()
        # Flappy:-
        self.flappy.play(dt)
        if self.flappy.is_alive:
            self.handle_bg.move(dt)
        return True   # End by returning false
