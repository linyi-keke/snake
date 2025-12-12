import pygame


class Score:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.setting = game.setting

    def write_score(self, game, filename="data.txt"):
        # 每次游戏结束时，记录一次当前游戏分数
        try:
            with open(filename, 'a', encoding='utf-8') as f:
                f.write(str(len(game.snake.bodies)) + '\n')
            return True
        except Exception as e:
            print(f"写入文件时出错: {e}")
            return False

    def read_score(self):
        # 每次游戏暂停或者结束时，读取分数
        pass

    def font(self):
        # 每次游戏暂停或者结束时，显示游戏历史最高分、当前分数
        pass

    def draw(self):
        pass

