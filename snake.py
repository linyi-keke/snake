import pygame


class Snake:
    def __init__(self, game):
        # 初始化贪吃蛇类
        self.screen = game.screen  # 游戏主屏幕
        self.screen_rect = game.screen_rect  # 屏幕矩形区域
        self.setting = game.setting  # 游戏设置对象

        # 创建蛇头矩形
        self.head = pygame.Rect(0, 0, self.setting.snake_width, self.setting.snake_height)
        self.head.center = self.screen_rect.center  # 蛇头初始位置在屏幕中心

        # 蛇的移动方向
        self.direction = 'right'  # 当前方向
        self.next_direction = 'right'  # 下一帧方向（用于防止连续按键导致反向移动）

        # 蛇身体部分，存储每个身体段的坐标
        self.bodies = []
        start_x = self.head.centerx
        start_y = self.head.centery
        self.bodies.append((start_x, start_y))  # 初始只有蛇头

        self.grow_pending = 0  # 待增长的身体段数

    def update_head_position(self):
        # 根据身体列表更新蛇头矩形位置
        if self.bodies:
            head_x, head_y = self.bodies[0]
            self.head.x = head_x
            self.head.y = head_y

    def change_direction(self, new_direction):
        # 改变蛇的移动方向，防止直接反向移动
        opposites = {'up': 'down', 'down': 'up', 'right': 'left', 'left': 'right'}
        if new_direction != opposites.get(self.direction):
            self.next_direction = new_direction

    def move(self, game):
        # 移动蛇
        self.direction = self.next_direction
        head_x, head_y = self.bodies[0]

        # 根据方向更新头部坐标
        if self.direction == 'right':
            head_x += self.setting.snake_speed
        elif self.direction == 'left':
            head_x -= self.setting.snake_speed
        elif self.direction == 'up':
            head_y -= self.setting.snake_speed
        elif self.direction == 'down':
            head_y += self.setting.snake_speed

        # 边界检测：撞墙则游戏结束
        if (head_x < 0 or head_x >= self.setting.screen_width or
                head_y < 0 or head_y >= self.setting.screen_height):
            game.pause_switch = False
            game.score.write_score(game)
            game.replay.reset_parameters(game)
            return

        new_head = (head_x, head_y)

        # 碰撞检测：撞到自己则游戏结束
        if new_head in self.bodies:
            game.pause_switch = False
            game.score.write_score(game)
            game.replay.reset_parameters(game)
            return

        # 在身体列表开头插入新的头部位置
        self.bodies.insert(0, new_head)

        self.update_head_position()  # 更新蛇头矩形位置

        # 如果不需要增长，则移除尾部
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.bodies.pop()

    def crash_test(self):
        # 吃到食物后增加身体长度
        self.grow_pending += 1

    def draw_snake(self):
        # 绘制整条蛇（包括头部和身体）
        for bodies in self.bodies:
            # 为每个身体段创建矩形并绘制
            rect = pygame.Rect(bodies[0], bodies[1], self.setting.snake_width, self.setting.snake_height)
            pygame.draw.rect(self.screen, self.setting.snake_color, rect)