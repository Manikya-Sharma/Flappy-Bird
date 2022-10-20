import pygame
from settings import Settings
from start_screen import Start
from end_screen import End
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
        self.ending = False
        self.final_score = 0
        self.medal = None
        self.start = Start()
        self.level = Level()
        self.end = End()

    def ascertain_medal(self):
        stat_file = open('../data/stats.txt', 'r+')
        data = stat_file.read()
        stat_file.close()
        # Analyze current data to statistics
        prev_scores = []
        for score in data.split(','):
            if not score.isdigit():
                continue
            prev_scores.append(int(score))
        try:
            self.max_score = max(prev_scores)
        except ValueError:
            self.max_score = 0

        i = 0
        for score in sorted(prev_scores):
            if self.final_score < score:
                i += 1
        if i == 0:
            self.medal = "platinum"
        elif i == 1:
            self.medal = "gold"
        elif i == 2:
            self.medal = "silver"
        elif i == 3:
            self.medal = "bronze"

        if self.final_score == 0:
            self.medal = None 

    def end_game(self):
        self.ending = True
        self.running = False
        self.ascertain_medal()
        # Add the data to statistics
        stat_file = open('../data/stats.txt', 'r+')
        data = stat_file.read()
        data = data +  str(self.final_score) + ","
        stat_file.seek(0)
        stat_file.write(data)
        stat_file.close()

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
                #         self.end.play()
            pygame.display.update()
            if not self.running:
                self.end_game() # To add statistics


        while self.ending:
            self.ending = self.end.play(self.final_score, self.max_score, self.medal)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.ending = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.ending = False

if __name__ == "__main__":
    game = Game()
    game.play()
