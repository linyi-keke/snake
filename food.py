import pygame
import random


class Food:
    def __init__(self, game):
        # 初始化食物类
        self.screen = game.screen  # 游戏主屏幕
        self.screen_rect = game.screen_rect  # 屏幕矩形区域
        self.setting = game.setting  # 游戏设置对象

        # 创建食物矩形
        self.food = pygame.Rect(0, 0, self.setting.food_width, self.setting.food_height)
        self.color = self.setting.food_color  # 食物颜色

        self.is_eaten = False  # 食物是否被吃掉的状态

        self.randomize_position(game.snake)  # 随机生成初始位置

    def randomize_position(self, snake):
        # 随机生成食物位置（确保在屏幕内）
        max_x = self.screen_rect.width - self.food.width
        max_y = self.screen_rect.height - self.food.height
        # 检测食物随机位置是否与蛇身有碰撞，若有就重新生成随机位置
        for i in range(100):
            x = random.randint(0, max_x)
            y = random.randint(0, max_y)

            food_v = pygame.Rect(x, y, self.setting.food_width, self.setting.food_height)

            collision = False
            for body_x, body_y in snake.bodies:
                body_v = pygame.Rect(body_x, body_y, snake.setting.snake_width, snake.setting.snake_height)

                if food_v.colliderect(body_v):
                    collision = True
                    break

            if not collision:
                self.food.x = x
                self.food.y = y
                break
        return

    def crash_test(self, snake):
        # 碰撞检测：检测蛇头是否碰到食物
        if self.food.colliderect(snake.head):
            self.is_eaten = True
            return True
        return False

    def draw_food(self):
        # 绘制食物（如果未被吃掉）
        if not self.is_eaten:
            pygame.draw.rect(self.screen, self.color, self.food)
