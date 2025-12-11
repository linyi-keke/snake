import pygame


class Pause1:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen_rect

        self.setting = game.setting

        original_image = pygame.image.load('暂停1.png')
        self.image = pygame.transform.scale(original_image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (self.setting.pause1_button_x, self.setting.pause1_button_y)

    def is_clicked(self, event, game):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            game.pause_switch = True

    def draw(self, game):
        if not game.pause_switch:
            self.screen.blit(self.image, self.rect)
