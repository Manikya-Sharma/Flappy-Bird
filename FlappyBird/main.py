import pygame
from settings import Settings
from start_screen import Start
from level import Level


class Game:
    def __init__(self):
        # Initialize
        pygame.init()
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()

        # Settings
        # TODO Add make defaults in settings panel of initialize screen
        self.data = Settings.get_settings()

        # Screen
        self.screen = pygame.display.set_mode(
            (int(self.data["SCREEN_WIDTH"]), int(self.data["SCREEN_HEIGHT"])))

        # Variables
        self.before_begin = True
        self.running = True
        self.final_score = 0
        self.start = Start()
        self.level = Level()

    def end_game(self):
        stat_file = open('../data/stats.txt', 'r+')
        data = stat_file.read()
        data = data +  str(self.final_score) + ","
        stat_file.seek(0)
        stat_file.write(data)
        stat_file.close()
        self.running = False

    def play(self):
        # Game loop
        while self.running:
            dt = self.clock.tick()/1000
            if self.before_begin:
                self.before_begin = self.start.play()
                if not self.before_begin:
                    self.level.initialize()
            else:
                self.running, self.final_score = self.level.play(dt)

            # Close Button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end_game()
                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_ESCAPE:
                #         self.end_game()
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.play()
    print("Game Over")
