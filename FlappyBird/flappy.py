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
        self.rotation = self.data["ROTATION"]
        self.rotation_speed = self.data["ROTATION_SPEED"]

    def get_speed(self):
        return float(self.speed)

    def get_color(self):
        return self.color

    def get_gravity(self):
        return float(self.gravity)

    def get_jump_intensity(self):
        return float(self.jump_intensity)

    def get_rotation(self):
        return float(self.rotation)

    def get_rotation_speed(self):
        return float(self.rotation_speed)

class Flappy:
    d = Defaults()
    def __init__(self, pos_x, pos_y, color=d.get_color(), x_speed = d.get_speed(),
                 initially_moving = False, inhibit_jump = True,
                 gravity = d.get_gravity(),
                 initial_rotation = d.get_rotation(),
                 rotation_speed = d.get_rotation_speed(),
                 init_status="idle", init_vel_y = 0):

        self.is_alive = True

        # Images
        self.blue_image = Images().get_flappy_blue_images()
        self.red_image = Images().get_flappy_red_images()
        self.yellow_image = Images().get_flappy_yellow_images()
        self.color = color
        if color == "yellow":
            self.images = self.yellow_image
        elif color == "red":
            self.images = self.red_image
        elif color == "blue":
            self.images = self.blue_image

        self.screen = pygame.display.get_surface()

        # Position
        self.pos_x = pos_x
        self.pos_y = pos_y

        # X motion
        self.x_speed = x_speed
        self.is_moving = initially_moving
        self.inhibit_jump = inhibit_jump

        # Y motion
        self.jump_timer = Timer()
        self.gravity = gravity
        self.vel_y = 0
        self.init_pos_y = pos_y
        self.init_vel_y = init_vel_y
        self.jump_intensity = -Defaults().get_jump_intensity()

        self.ignore_timer = Timer() # To prevent excess jump

        # Rotation
        self.initial_rotation =initial_rotation
        self.rotation = self.initial_rotation
        self.rotation_speed = rotation_speed

        # Status
        self.status = init_status
        self.image = self.images[self.status]

        # Offset
        # Default position x of bird = width/3
        # Bird draws on offset but position on pos_x
        self.offset_x = self.pos_x - self.screen.get_size()[0]/3


    def draw(self):
        self.screen.blit(self.image, (self.pos_x - self.offset_x, self.pos_y))

    def update_status(self):
        # up/down
        if self.vel_y > 0:
            self.status = "down"
        elif self.vel_y < 0:
            self.status = "up"
        else:
            self.status = "idle"

        self.image = self.images[self.status]

    def update_fall(self, dt):
        # Die
        if self.pos_y+self.image.get_height() >= pygame.display.get_window_size()[1]:
            self.gravity = 0
            self.vel_y = 0
            self.pos_y = pygame.display.get_window_size()[1]-self.image.get_height()
            self.init_pos_y = self.pos_y
            self.die()
            return

        jump_time = self.jump_timer.time_elapsed()
        self.pos_y = \
        self.init_pos_y + self.init_vel_y*jump_time+(1/2)*(self.gravity)*(jump_time**2)
        self.vel_y = self.init_vel_y+(self.gravity*jump_time)


    def update_rotation(self, dt):
        if self.rotation >= -40:
            self.rotation -= self.rotation_speed*dt

    def update_image_rotation(self):
        self.image = pygame.transform.rotate(self.image, self.rotation)
        pygame.display.get_surface().blit(self.image, (0,0))

    def move(self, dt):
        # move forward
        if self.is_moving:
            self.pos_x += self.x_speed*dt
        self.offset_x = self.pos_x - self.screen.get_size()[0]/3

    def change_color(self, color):
        if color.lower() in ("red", "yellow", "blue"):
            self.color = color.lower()

    def start_moving(self):
        self.is_moving = True
        self.inhibit_jump = False

    def stop_moving(self):
        self.is_moving = False
        self.inhibit_jump = True

    def start_jumping(self):
        if not self.inhibit_jump:
            # Jump
            self.jump_timer.restart()
            self.vel_y = self.jump_intensity
            self.init_pos_y = self.pos_y
            self.init_vel_y = self.vel_y
            # Give flap effect
            self.status = 'idle'
            self.image = self.images[self.status]

            #Rotation
            self.rotation = self.initial_rotation

    def update(self, dt):
        self.update_status()
        self.update_image_rotation()
        self.update_fall(dt)
        self.update_rotation(dt)

    def play(self, dt):
        # integrate all methods
        self.update(dt)
        self.move(dt)
        self.draw()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.start_jumping()
            self.ignore_timer.restart()
        if keys[pygame.K_ESCAPE]:
            self.die()

    def die(self):
        self.is_alive = False
        self.stop_moving()
        self.rotation = -90
