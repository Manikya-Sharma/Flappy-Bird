import pygame
from settings import Settings


class Images:
    def __init__(self):
        self.data = Settings.get_settings()

        self.bg_images = \
            {
                "day": pygame.image.load("../Animations/Background/day.png"),
                "night": pygame.image.load("../Animations/Background/night.png")
            }
        self.flappy_blue_images = \
            {
                "down": pygame.image.load("../Animations/Flappy/blue/flappy_down.png"),
                "idle": pygame.image.load("../Animations/Flappy/blue/flappy_idle.png"),
                "up": pygame.image.load("../Animations/Flappy/blue/flappy_up.png")
            }
        self.flappy_red_images = \
            {
                "down": pygame.image.load("../Animations/Flappy/red/flappy_down.png"),
                "idle": pygame.image.load("../Animations/Flappy/red/flappy_idle.png"),
                "up": pygame.image.load("../Animations/Flappy/red/flappy_up.png")
            }
        self.flappy_yellow_images = \
            {
                "down": pygame.image.load("../Animations/Flappy/yellow/flappy_down.png"),
                "idle": pygame.image.load("../Animations/Flappy/yellow/flappy_idle.png"),
                "up": pygame.image.load("../Animations/Flappy/yellow/flappy_up.png")
            }
        self.ground_images = \
            {
                "ground": pygame.image.load("../Animations/Ground/ground.png")
            }
        self.number_images = \
            {
                "0": pygame.image.load("../Animations/Numbers/number_0.png"),
                "1": pygame.image.load("../Animations/Numbers/number_1.png"),
                "2": pygame.image.load("../Animations/Numbers/number_2.png"),
                "3": pygame.image.load("../Animations/Numbers/number_3.png"),
                "4": pygame.image.load("../Animations/Numbers/number_4.png"),
                "5": pygame.image.load("../Animations/Numbers/number_5.png"),
                "6": pygame.image.load("../Animations/Numbers/number_6.png"),
                "7": pygame.image.load("../Animations/Numbers/number_7.png"),
                "8": pygame.image.load("../Animations/Numbers/number_8.png"),
                "9": pygame.image.load("../Animations/Numbers/number_9.png"),
            }
        self.pillar_images = \
            {
                "brown": pygame.image.load("../Animations/Pillar/brown_pillar.png"),
                "green": pygame.image.load("../Animations/Pillar/green_pillar.png"),
            }
        self.ui_images = \
            {
                "flappy_bird": pygame.image.load("../Animations/Ui/flappy_bird.png"),
                "play_button": pygame.image.load("../Animations/Ui/play_button.png"),
                "menu": pygame.image.load("../Animations/Ui/menu.png"),
                "ok": pygame.image.load("../Animations/Ui/ok.png"),
                "get_ready": pygame.image.load("../Animations/Ui/get_ready.png"),
                "pause_button": pygame.image.load("../Animations/Ui/pause_button.png"),
                "game_over": pygame.image.load("../Animations/Ui/game_over.png"),
                "score_card": pygame.image.load("../Animations/Ui/score_card.png"),
                "platinum_medal": pygame.image.load("../Animations/Ui/platinum_medal.png"),
                "gold_medal": pygame.image.load("../Animations/Ui/gold_medal.png"),
                "silver_medal": pygame.image.load("../Animations/Ui/silver_medal.png"),
                "bronze_medal": pygame.image.load("../Animations/Ui/bronze_medal.png"),
            }

    def get_bg_images(self):
        return self.prepare_images(self.bg_images, True)

    def get_flappy_blue_images(self):
        return self.prepare_images(self.flappy_blue_images)

    def get_flappy_yellow_images(self):
        return self.prepare_images(self.flappy_yellow_images)

    def get_flappy_red_images(self):
        return self.prepare_images(self.flappy_red_images)

    def get_ground_images(self):
        return self.prepare_images(self.ground_image)

    def get_number_images(self):
        return self.prepare_images(self.number_images)

    def get_pillar_images(self):
        return self.prepare_images(self.pillar_images)

    def get_ui_images(self):
        return self.prepare_images(self.ui_images)

    def prepare_images(self, dic, bg_image=False):
        new_dic = {}
        for key, val in dic.items():
            if bg_image:
                new_val = pygame.transform.scale(
                    val, (int(self.data["SCREEN_WIDTH"]), int(self.data["SCREEN_HEIGHT"])))
            else:
                new_val = pygame.transform.scale2x(val)
            new_dic[key] = new_val
        return new_dic
