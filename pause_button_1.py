import pygame


class Pause1:
    def __init__(self, game):
        # 初始化暂停界面大按钮类
        self.screen = game.screen  # 游戏主屏幕
        self.screen_rect = game.screen_rect  # 屏幕矩形区域

        self.setting = game.setting  # 游戏设置对象

        # 加载并缩放暂停界面大按钮图片
        original_image = pygame.image.load('暂停1.png')
        self.image = pygame.transform.scale(original_image, (100, 100))
        self.rect = self.image.get_rect()  # 获取图片矩形区域
        # 设置按钮位置（屏幕中央）
        self.rect.center = (self.setting.pause1_button_x, self.setting.pause1_button_y)

    def draw(self, game):
        # 在屏幕上绘制按钮（仅在游戏暂停时显示）
        if not game.pause_switch:
            self.screen.blit(self.image, self.rect)