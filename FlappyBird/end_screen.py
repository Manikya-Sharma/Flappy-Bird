import pygame
from images import Images

class End:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.image_handler = Images()
        self.medals_images = [
            self.image_handler.get_ui_images()["bronze_medal"],
            self.image_handler.get_ui_images()["silver_medal"],
            self.image_handler.get_ui_images()["gold_medal"],
            self.image_handler.get_ui_images()["platinum_medal"]]
        self.score_card_image = self.image_handler.get_ui_images()["score_card"]
        self.ok_image = self.image_handler.get_ui_images()["ok"]

        self.font_face = "freesansbold.ttf"
        self.font_size = 20
        self.font = pygame.font.Font(self.font_face, self.font_size)

    def draw(self, final_score, max_score, medal):
        if final_score > max_score:
            max_score = final_score # Just to show this is max

        w = self.screen.get_size()[0]
        h = self.screen.get_size()[1]
        # Score Card
        self.screen.blit(self.score_card_image,
        (w/2-self.score_card_image.get_width()/2,
        h/2-self.score_card_image.get_height()/2))

        # Medal
        if medal is not None:
            if medal == "bronze":
                medal_image = self.medals_images[0]
            elif medal == "silver":
                medal_image = self.medals_images[1]
            elif medal == "gold":
                medal_image = self.medals_images[2]
            elif medal == "platinum":
                medal_image = self.medals_images[3]
            self.screen.blit(medal_image,
            (w/2-self.score_card_image.get_width()/2\
                + 25,
                h/2-self.score_card_image.get_height()/2\
                    +45))

        # Your score
        score_text = self.font.render(str(final_score), True, (0,0,0))
        self.screen.blit(score_text, (w/2+57, h/2-27))

        # Best score
        best_score_text = self.font.render(str(max_score), True, (0,0,0))
        self.screen.blit(best_score_text, (w/2+57, h/2+17))

    def play(self, final_score, max_score, medal):
        self.draw(final_score, max_score, medal)
        pygame.display.update()
        if pygame.mouse.get_pressed()[0]:
            return False
        return True