import pygame
import random


class Food:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.setting = game.setting

        self.food = pygame.Rect(0, 0, self.setting.food_width, self.setting.food_height)
        self.color = self.setting.food_color

        self.is_eaten = False

        self.randomize_position()

    def randomize_position(self):
        max_x = self.screen_rect.width - self.food.width
        max_y = self.screen_rect.height - self.food.height

        self.food.x = random.randint(0, max_x)
        self.food.y = random.randint(0, max_y)

    def crash_test(self, snake):
        if self.food.colliderect(snake.head):
            self.is_eaten = True
            return True
        return False

    def draw_food(self):
        if not self.is_eaten:
            pygame.draw.rect(self.screen, self.color, self.food)

