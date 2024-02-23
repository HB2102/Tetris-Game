from settings import *
from sys import exit
from os.path import join
from game import Game
from score import Score
from preview import Preview
from random import choice


class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Tetris')

        self.next_shapes = [choice(list(TETROMINOS.keys())) for shape in range(3)]
        self.game = Game(self.get_next_shape, self.update_score)
        self.score = Score()
        self.preview = Preview()

        self.music = pygame.mixer.Sound(join('.', 'sounds', 'music.wav'))
        self.music.set_volume(0.05)
        self.music.play(-1)

    def get_next_shape(self):
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(TETROMINOS.keys())))
        return next_shape

    def update_score(self, lines, score, level):
        self.score.lines = lines
        self.score.score = score
        self.score.level = level

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.display_surface.fill(GRAY)
            self.game.run()
            self.score.run()
            self.preview.run(self.next_shapes)

            pygame.display.update()
            self.clock.tick()


if __name__ == '__main__':
    main = Main()
    main.run()
