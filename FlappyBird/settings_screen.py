import pygame
from settings import Settings
from images import Images

"""
Settings: Change time
          Change pillar color
          Change flappy color
          Make settings default
"""

class Settings_Screen:
    def __init__(self):
        self.screen = pygame.display.get_surface()

        self.data = Settings.get_settings()
        self.image_provider = Images()

        # Images to show
        # UI
        self.ui_images = self.image_provider.get_ui_images()

        # TIME
        self.bg_images = self.image_provider.get_bg_images()
        self.day_option_image = Settings_Screen.prepare_option_images(self.bg_images["day"])
        self.night_option_image = Settings_Screen.prepare_option_images(self.bg_images["night"])

        # FLAPPY
        self.flappy_frame = 0
        self.flappy_frame_speed = 70
        self.flappy_statuses = ["down", "idle", "up"]
        self.current_flappy_status = 0

        self.flappy_images = {
            "blue": self.image_provider.get_flappy_blue_images(),
            "red": self.image_provider.get_flappy_red_images(),
            "yellow": self.image_provider.get_flappy_yellow_images()
        }

        self.flappy_option_image_size = 40
        self.flappy_yellow_option_image = Settings_Screen.prepare_option_images(
            self.flappy_images["yellow"][self.flappy_statuses[self.current_flappy_status]],
            (self.flappy_option_image_size,self.flappy_option_image_size))
        self.flappy_blue_option_image = Settings_Screen.prepare_option_images(
            self.flappy_images["blue"][self.flappy_statuses[self.current_flappy_status]],
            (self.flappy_option_image_size,self.flappy_option_image_size))
        self.flappy_red_option_image = Settings_Screen.prepare_option_images(
            self.flappy_images["red"][self.flappy_statuses[self.current_flappy_status]],
            (self.flappy_option_image_size,self.flappy_option_image_size))

        #Pillar
        self.pillar_images = self.image_provider.get_pillar_images()
        self.green_pillar_option_image = Settings_Screen.prepare_option_images(
            self.pillar_images["green"])
        self.brown_pillar_option_image = Settings_Screen.prepare_option_images(
            self.pillar_images["brown"])

        # Background
        self.bg_image =self.image_provider.get_bg_images()[self.data["TIME"]]
        self.ground_image = self.image_provider.get_ground_images()["ground"]

        self.font_face = "freesansbold.ttf"
        self.font_size = 20
        self.padding = 40
        if self.data["TIME"] == "day":
            self.font_color = (0,0,0)
            self.selection_box_color = (255,0,0)
        else:
            self.font_color = (255,255,255)
            self.selection_box_color = (255, 255, 0)
        self.font = pygame.font.Font(self.font_face, self.font_size)

        # Ok option
        self.ok_text = self.font.render("Ok", True, (0,0,0))

    def animate(self):
        self.flappy_frame += 1

        if self.flappy_frame == self.flappy_frame_speed:
            self.flappy_frame = 0
            if self.current_flappy_status==2:
                self.current_flappy_status = 0
            else:
                self.current_flappy_status += 1

        self.flappy_yellow_option_image = Settings_Screen.prepare_option_images(
            self.flappy_images["yellow"][self.flappy_statuses[self.current_flappy_status]],
            (self.flappy_option_image_size,self.flappy_option_image_size))
        self.flappy_blue_option_image = Settings_Screen.prepare_option_images(
            self.flappy_images["blue"][self.flappy_statuses[self.current_flappy_status]],
            (self.flappy_option_image_size,self.flappy_option_image_size))
        self.flappy_red_option_image = Settings_Screen.prepare_option_images(
            self.flappy_images["red"][self.flappy_statuses[self.current_flappy_status]],
            (self.flappy_option_image_size,self.flappy_option_image_size))

    def draw(self):
        width, height = self.screen.get_size()

        # Background
        self.screen.blit(self.bg_image, (0,0))
        self.screen.blit(self.ground_image,
        (0, height-self.ground_image.get_height()))

        # Time Option
            # Text
        time_option_text = self.font.render("Time", True, self.font_color)
        self.screen.blit(time_option_text, (self.padding, self.padding))

            # Images
        day_x_pos = self.padding+time_option_text.get_width()+self.padding
        self.screen.blit(self.day_option_image,
         (day_x_pos, self.padding))

        night_x_pos = day_x_pos+self.day_option_image.get_width()+self.padding
        self.screen.blit(self.night_option_image,
         (night_x_pos, self.padding))

            # Selection Rectangle
        if self.data["TIME"] == "day":
            pygame.draw.rect(self.screen, self.selection_box_color,
            [day_x_pos-3, self.padding-3, self.day_option_image.get_width()+6,
            self.day_option_image.get_height()+6], 2)
        else:
            pygame.draw.rect(self.screen, self.selection_box_color,
            [night_x_pos-3, self.padding-3, self.night_option_image.get_width()+6,
            self.night_option_image.get_height()+6], 2)

        # Flappy Option
            # Text
        max_y_pos_flappy_option = max(
            [time_option_text.get_height(),
            self.day_option_image.get_height(),
            self.night_option_image.get_height()])
        flappy_option_y_pos = max_y_pos_flappy_option+2*self.padding
        flappy_option_text = self.font.render("Flappy", True, self.font_color)
        self.screen.blit(flappy_option_text,
        (self.padding, flappy_option_y_pos))


            # Flappy yellow image
        yellow_image_option_x = self.padding+flappy_option_text.get_width()+self.padding
        self.screen.blit(self.flappy_yellow_option_image,
        (yellow_image_option_x, flappy_option_y_pos))

            # Flappy yellow image
        red_image_option_x = yellow_image_option_x+ self.flappy_yellow_option_image.get_width()\
        + self.padding
        self.screen.blit(self.flappy_red_option_image,
        (red_image_option_x, flappy_option_y_pos))

            # Flappy yellow image
        blue_image_option_x = red_image_option_x+ self.flappy_red_option_image.get_width()\
        + self.padding
        self.screen.blit(self.flappy_blue_option_image,
        (blue_image_option_x, flappy_option_y_pos))

        if self.data["COLOR"] == "yellow":
            pygame.draw.rect(self.screen, self.selection_box_color,
            [yellow_image_option_x-3, flappy_option_y_pos-3,
            self.flappy_yellow_option_image.get_width()+6,
            self.flappy_yellow_option_image.get_height()+6], 2)
        elif self.data["COLOR"] == "blue":
            pygame.draw.rect(self.screen, self.selection_box_color,
            [blue_image_option_x-3, flappy_option_y_pos-3,
            self.flappy_blue_option_image.get_width()+6,
            self.flappy_blue_option_image.get_height()+6], 2)
        elif self.data["COLOR"] == "red":
            pygame.draw.rect(self.screen, self.selection_box_color,
            [red_image_option_x-3, flappy_option_y_pos-3,
            self.flappy_red_option_image.get_width()+6,
            self.flappy_red_option_image.get_height()+6], 2)

        # Pillar Option
        max_y_pos_pillar_option = max(
            [flappy_option_text.get_height(),
            self.flappy_yellow_option_image.get_height(),
            self.flappy_blue_option_image.get_height(),
            self.flappy_red_option_image.get_height()
            ])
        pillar_option_y_pos = flappy_option_y_pos+ max_y_pos_pillar_option+self.padding

            # Text
        pillar_option_text = self.font.render("Pillar", True, self.font_color)
        self.screen.blit(pillar_option_text, (self.padding, pillar_option_y_pos))

            # Images
        green_pillar_x_pos = self.padding+pillar_option_text.get_width()+self.padding
        self.screen.blit(self.green_pillar_option_image,
         (green_pillar_x_pos, pillar_option_y_pos))

        brown_pillar_x_pos = green_pillar_x_pos+self.brown_pillar_option_image.get_width()+self.padding
        self.screen.blit(self.brown_pillar_option_image,
         (brown_pillar_x_pos, pillar_option_y_pos))

            # Selection Rectangle
        if self.data["PILLAR_COLOR"] == "green":
            pygame.draw.rect(self.screen, self.selection_box_color,
            [green_pillar_x_pos-3, pillar_option_y_pos-3, self.green_pillar_option_image.get_width()+6,
            self.day_option_image.get_height()+6], 2)
        else:
            pygame.draw.rect(self.screen, self.selection_box_color,
            [brown_pillar_x_pos-3, pillar_option_y_pos-3, self.brown_pillar_option_image.get_width()+6,
            self.day_option_image.get_height()+6], 2)

        # Apply Settings Button
        pygame.draw.rect(self.screen, (255,255,255),
        [width-self.padding-self.ok_text.get_width()-3, height-self.padding-self.ok_text.get_height()-3,
        self.ok_text.get_width()+6, self.ok_text.get_height()+6])
        self.screen.blit(self.ok_text,
        (width-self.padding-self.ok_text.get_width(),
        height-self.padding-self.ok_text.get_height()))

    def run(self):
        self.animate()
        self.draw()
        return True # Keep settings screen

    @staticmethod
    def prepare_option_images(image, size = (100,100)):
        image = pygame.transform.scale(image, size)
        return image