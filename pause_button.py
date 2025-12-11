import pygame


class Pause:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen_rect

        self.setting = game.setting

        original_image = pygame.image.load('暂停.png')
        self.image = pygame.transform.scale(original_image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (self.setting.pause_button_x, self.setting.pause_button_y)

    def is_clicked(self, event, game):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            game.pause_switch = False

    def draw(self):
        self.screen.blit(self.image, self.rect)
