import pygame


class Snake:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.setting = game.setting

        self.head = pygame.Rect(0, 0, self.setting.snake_width, self.setting.snake_height)
        self.head.center = self.screen_rect.center

        self.direction = 'right'
        self.next_direction = 'right'

        self.bodies = []
        start_x = self.head.centerx
        start_y = self.head.centery
        self.bodies.append((start_x, start_y))

        self.grow_pending = 0

    def update_head_position(self):
        if self.bodies:
            head_x, head_y = self.bodies[0]
            self.head.x = head_x
            self.head.y = head_y

    def change_direction(self, new_direction):
        opposites = {'up': 'down', 'down': 'up', 'right': 'left', 'left': 'right'}
        if new_direction != opposites.get(self.direction):
            self.next_direction = new_direction

    def move(self, game):
        self.direction = self.next_direction
        head_x, head_y = self.bodies[0]

        if self.direction == 'right':
            head_x += self.setting.snake_speed
        elif self.direction == 'left':
            head_x -= self.setting.snake_speed
        elif self.direction == 'up':
            head_y -= self.setting.snake_speed
        elif self.direction == 'down':
            head_y += self.setting.snake_speed

        if (head_x < 0 or head_x >= self.setting.screen_width or
                head_y < 0 or head_y >= self.setting.screen_height):
            game.running = False
            return

        new_head = (head_x, head_y)

        if new_head in self.bodies:
            game.running = False
            return

        self.bodies.insert(0, new_head)

        self.update_head_position()

        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.bodies.pop()

    def crash_test(self):
        self.grow_pending += 1

    def draw_snake(self):
        for bodies in self.bodies:
            rect = pygame.Rect(bodies[0], bodies[1], self.setting.snake_width, self.setting.snake_height)
            pygame.draw.rect(self.screen, self.setting.snake_color, rect)

