import pygame
from settings import Settings
from start_screen import Start
from level import Level


class Game:
    def __init__(self):
        # Initialize
        pygame.init()
        pygame.display.set_caption("Flappy Bird")

        # Settings
        # TODO Add make defaults in settings panel of initialize screen
        self.s = Settings()
        try:
            file = open('../data/data.txt', 'r+')
        except FileNotFoundError:
            file = open('../data/data.txt', 'w+')
            file.write('0')
            file.seek(0)

        data = file.read()
        if data.strip() == '0':  # This is first time game was opened
            file.seek(0)
            file.write('1')
            Settings.make_default_settings()

        file.close()
        self.data = Settings.get_settings()

        self.screen = pygame.display.set_mode(
            (int(self.data["SCREEN_WIDTH"]), int(self.data["SCREEN_HEIGHT"])))

        # Variables
        self.before_begin = True
        self.running = True
        self.start = Start()
        self.level = Level()

    def end_game(self):
        self.running = False

    def play(self):
        # Game loop
        while self.running:
            if self.before_begin:
                self.before_begin = self.start.play()
            else:
                self.running = self.level.play()

            # Close Button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end_game()

if __name__ == "__main__":
    game = Game()
    game.play()
    print("Game Over")
