import pygame
import settings
from snake import Snake
from food import Food


class Game:
    def __init__(self):
        pygame.init()
        self.setting = settings.Settings()
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("贪吃蛇2")
        self.bg_color = self.setting.bg_color
        self.clock = pygame.time.Clock()
        self.running = True

        self.move_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.move_event, 120)

        self.snake = Snake(self)
        self.food = Food(self)

    def event_track(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == self.move_event:
                self.snake.move(self)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction('up')
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction('down')
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction('right')
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction('left')

    def collide_detection(self):
        if self.food.crash_test(self.snake):
            self.food.randomize_position()
            self.food.is_eaten = False
            self.snake.crash_test()

    def draw_screen(self):
        self.screen.fill(self.bg_color)
        self.snake.draw_snake()
        self.food.draw_food()

    def run_game(self):
        while self.running:
            self.event_track()
            self.collide_detection()
            self.draw_screen()
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run_game()
