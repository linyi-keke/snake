import pygame


class Replay:
    def __init__(self, game):
        # 初始化重玩按钮类
        self.screen = game.screen  # 游戏主屏幕
        self.screen_rect = game.screen_rect  # 屏幕矩形区域

        self.setting = game.setting  # 游戏设置对象

        # 加载并缩放重玩按钮图片
        original_image = pygame.image.load('重玩.png')
        self.image = pygame.transform.scale(original_image, (50, 50))
        self.rect = self.image.get_rect()  # 获取图片矩形区域
        # 设置按钮位置
        self.rect.center = (self.setting.replay_button_x, self.setting.replay_button_y)

    def is_clicked(self, event):
        # 检测按钮是否被点击（当前为空实现）
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            return True
        return False

    def draw(self):
        # 在屏幕上绘制重玩按钮
        self.screen.blit(self.image, self.rect)
