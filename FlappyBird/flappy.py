import pygame
from timer import Timer
from settings import Settings
from images import Images

class Defaults:
    def __init__(self):
        self.data = Settings().get_settings()
        self.speed = self.data["X_SPEED"]
        self.color = self.data["COLOR"]
        self.gravity = self.data["GRAVITY"]
        self.jump_intensity = self.data["JUMP_INTENSITY"]

    def get_speed(self):
        return float(self.speed)

    def get_color(self):
        return self.color

    def get_gravity(self):
        return float(self.gravity)

    def get_jump_intensity(self):
        return float(self.jump_intensity)

class Flappy:
    d = Defaults()
    def __init__(self, pos_x, pos_y, color=d.get_color(), x_speed = d.get_speed(),
                 initially_moving = False, gravity = d.get_gravity(),
                 init_status="idle", init_vel_y = -d.get_jump_intensity()):
        # Images
        self.blue_image = Images().get_flappy_blue_images()
        self.red_image = Images().get_flappy_red_images()
        self.yellow_image = Images().get_flappy_yellow_images()
        self.color = color
        self.screen = pygame.display.get_surface()
        # Position
        self.pos_x = pos_x
        self.pos_y = pos_y
        # X motion
        self.x_speed = x_speed
        self.is_moving = initially_moving
        # Y motion
        self.jump_timer = Timer()
        self.gravity = gravity
        self.vel_y = 0
        self.init_pos_y = pos_y
        self.init_vel_y = init_vel_y
        # Status
        self.status = init_status

    def draw(self):
        self.screen.blit(self.yellow_image[self.status], (self.pos_x, self.pos_y))

    def update_status(self):
        # up/down
        if self.vel_y > 0:
            self.status = "down"
        elif self.vel_y < 0:
            self.status = "up"
        else:
            self.status = "idle"

    def update_fall(self, dt):
        # make it fall
        jump_time = self.jump_timer.time_elapsed()
        self.pos_y = self.init_pos_y +\
             self.init_vel_y*jump_time+(1/2)*(self.gravity)*(jump_time**2)

        self.vel_y = self.init_vel_y+(self.gravity*jump_time)

    def move(self, dt):
        # move forward
        if self.is_moving:
            self.pos_x += self.x_speed*dt

    def change_color(self, color):
        if color.lower() in ("red", "yellow", "blue"):
            self.color = color.lower()

    def start_moving(self):
        self.is_moving = True

    def stop_moving(self):
        self.is_moving = False

    def start_jumping(self):
        self.jump_timer.restart()
        self.vel_y = self.init_vel_y
        self.init_pos_y = self.pos_y

    def play(self, dt):
        # integrate all methods
        self.draw()
        self.update_status()
        self.update_fall(dt)
        self.start_moving() #TODO After pressing a key
        self.move(dt)
