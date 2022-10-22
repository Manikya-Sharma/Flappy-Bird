import pygame
from settings import Settings
from settings_screen import Settings_Screen
from images import Images


class Start:
    def __init__(self):
        self.keep_running = True
        self.run_settings = False
        self.settings_screen = Settings_Screen()
        self.screen = pygame.display.get_surface()

        # Data
        self.data = Settings.get_settings()
        self.image_provider = Images()
        self.images = self.image_provider.get_ui_images()
        self.bg_image = self.image_provider.get_bg_images()[self.data["TIME"]]
        self.ground_image = self.image_provider.get_ground_images()["ground"]

        # Top Score
        with open('../data/stats.txt', 'r') as file:
            data = file.read()
            if data.isspace() or data == '':
                self.max_score = 0
            else:
                lis = data.split(',')
                lis.pop(len(lis)-1)  # To remove blank
                for ind, score in enumerate(lis):
                    if not score.isdigit():
                        continue
                    lis[ind] = int(score)
                self.max_score = max(lis)

         # Buttons
        self.start_button_width = 150
        self.start_button_height = 50

        self.font = "freesansbold.ttf"
        self.font_size = 20
        self.padding = 40

        # Flappy Font
        self.flappy_font = "freesansbold.ttf"
        self.flappy_font_size = 60

    def draw(self):
        width, height = self.screen.get_size()
        # Background
        self.screen.blit(self.bg_image, (0, 0))
        self.screen.blit(self.ground_image,
                         (0, height-self.ground_image.get_height()))

        # Flappy Bird Text
        flappy_font = pygame.font.Font(self.flappy_font, self.flappy_font_size)
        flappy_text = flappy_font.render("Flappy Bird", True, (0, 0, 0))
        self.screen.blit(flappy_text,
                         (width/2-flappy_text.get_width()/2, 100))

        # Start Button
        pygame.draw.rect(self.screen, (255, 255, 255),
                         [width/2-self.start_button_width/2,
                          height/2 -
                          self.start_button_height/2,
                          self.start_button_width, self.start_button_height])

        # Start Text
        start_font = pygame.font.Font(self.font, self.font_size)
        start_text = start_font.render("START", True, (0, 0, 0))
        self.screen.blit(start_text,
                         (width/2-start_text.get_width()/2,
                          height/2-start_text.get_height()/2))

        # Settings Button
        pygame.draw.rect(self.screen, (255, 255, 255),
                         [width/2-self.start_button_width/2,
                          height/2 +
                          self.start_button_height/2+self.padding,
                          self.start_button_width, self.start_button_height])

        # Settings Text
        start_font = pygame.font.Font(self.font, self.font_size)
        start_text = start_font.render("SETTINGS", True, (0, 0, 0))
        self.screen.blit(start_text,
                         (width/2-start_text.get_width()/2,
                          height/2+self.start_button_height/2
                          + self.padding+start_text.get_height()/2))

    def detect_click(self, position):
        width, height = self.screen.get_size()
        pos_x, pos_y = position
        if (pos_x >= width/2 - self.start_button_width/2)\
            and (pos_x <= width/2 + self.start_button_width/2)\
                and (pos_y >= height)/2-self.start_button_height/2\
        and (pos_y <= height/2+self.start_button_height/2):
            return "START"

        if (pos_x >= width/2 - self.start_button_width/2)\
            and (pos_x <= width/2 + self.start_button_width/2)\
                and (pos_y >= height/2+self.start_button_height/2
                     + self.padding)\
        and (pos_y <= height/2+self.start_button_height/2\
                 + self.padding+self.start_button_height):
            return "SETTINGS"

    def play(self):
        if self.run_settings:
            self.run_settings = self.settings_screen.run()
            return True  # Never end

        self.draw()
        if pygame.mouse.get_pressed()[0]:
            clicked = self.detect_click(pygame.mouse.get_pos())
        else:
            clicked = False

        if clicked == "START":
            return False
        elif clicked == "SETTINGS":
            self.run_settings = True
            return True
        return True
