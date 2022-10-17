import pygame
from settings import Settings
from images import Images
from random import randint


class Defaults:
    def __init__(self):
        self.data = Settings().get_settings()
        self.color = self.data["PILLAR_COLOR"]

    def get_color(self):
        return self.color


class Pillar:
    """Note that pillars are static but due to offset seem moving"""
    d = Defaults()
    pillars_list = []
    pillars_max_list = []
    # Will store max bound of pillar width for record of score

    def __init__(self, flappy_bound, color=d.get_color(), init_x=None):
        # Initialize
        self.screen = pygame.display.get_surface()
        # Images
        self.color = color
        self.images = Images().get_pillar_images()
        self.image = self.images[color]
        self.width = self.image.get_width()
        self.ground_image = Images().get_ground_images()["ground"]
        self.ground_height =self.ground_image.get_height()

        # Initial position
        if init_x is None:
            self.init_x = pygame.display.get_window_size()[0]*(3/4)
        else:
            self.init_x = init_x
        # Position
        self.flappy_bound = flappy_bound
        self.pos_x = self.init_x
        self.speed = flappy_bound.x_speed
        self.offset_x = flappy_bound.offset_x

        # Pillar Heights
        self.pillar_gap = 140
        screen_height = self.screen.get_size()[1]
        rand_height = randint(20, screen_height-self.ground_height-self.pillar_gap-20)
        self.gap_y = rand_height

        self.pillar_height_1 = self.gap_y
        self.pillar_height_2 = screen_height - self.ground_height -self.gap_y - self.pillar_gap

        self.pos_1_y = 0
        self.pos_2_y = self.gap_y+self.pillar_gap

        Pillar.pillars_list.append(self)
        Pillar.pillars_max_list.append(self.pos_x+self.width)

    def update(self):
        self.offset_x = self.flappy_bound.offset_x

    def draw(self):
        img_1 = pygame.transform.flip(self.image, flip_x=False, flip_y=True)
        img_1 = pygame.transform.scale(
            img_1, (self.width, self.pillar_height_1))
        img_2 = pygame.transform.scale(
            self.image, (self.width, self.pillar_height_2))

        self.screen.blit(img_1,
                         (self.pos_x - self.offset_x, self.pos_1_y))
        self.screen.blit(img_2,
                         (self.pos_x - self.offset_x, self.pos_2_y))

    def play(self):
        self.update()
        self.draw()

    def is_collision(self):
        if (self.flappy_bound.pos_x+self.flappy_bound.image.get_width() >= self.pos_x
                and self.flappy_bound.pos_x <= self.pos_x+self.width):
            if (self.flappy_bound.pos_y >= self.gap_y
                and
                    self.flappy_bound.pos_y+self.flappy_bound.image.get_height() <= self.gap_y+self.pillar_gap):
                return False
            else:
                return True
        else:
            return False

    @classmethod
    def update_pillars_creation(cls, flappy, pillars_gap, screen_width):
        first_pillar = cls.pillars_list[0]
        final_pillar = cls.pillars_list[-1]
        if first_pillar.pos_x - first_pillar.offset_x + first_pillar.width <= 0:
            del cls.pillars_list[0]
        del first_pillar

        if final_pillar.pos_x - final_pillar.offset_x <= pillars_gap:
            Pillar(flappy, init_x=screen_width+final_pillar.offset_x)

    @classmethod
    def check_collisions(cls):
        for pillar in cls.pillars_list:
            has_collided = pillar.is_collision()
            if has_collided:
                return True
        return False
