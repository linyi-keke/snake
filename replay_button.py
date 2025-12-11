import pygame


class Replay:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen_rect

        self.setting = game.setting

        original_image = pygame.image.load('重玩.png')
        self.image = pygame.transform.scale(original_image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (self.setting.replay_button_x, self.setting.replay_button_y)

    def is_clicked(self):
        pass

    def draw(self):
        self.screen.blit(self.image, self.rect)
