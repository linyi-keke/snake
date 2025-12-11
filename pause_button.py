import pygame


class Pause:
    def __init__(self, game):
        # 初始化暂停按钮类
        self.screen = game.screen  # 游戏主屏幕
        self.screen_rect = game.screen_rect  # 屏幕矩形区域

        self.setting = game.setting  # 游戏设置对象

        # 加载并缩放暂停按钮图片
        original_image = pygame.image.load('暂停.png')
        self.image = pygame.transform.scale(original_image, (50, 50))
        self.rect = self.image.get_rect()  # 获取图片矩形区域
        # 设置按钮位置
        self.rect.center = (self.setting.pause_button_x, self.setting.pause_button_y)

    def is_clicked(self, event, game):
        # 检测按钮是否被点击
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            game.pause_switch = False  # 点击后暂停游戏

    def draw(self):
        # 在屏幕上绘制暂停按钮
        self.screen.blit(self.image, self.rect)