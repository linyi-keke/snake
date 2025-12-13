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

    def read_score(self, filename='data.txt'):
        # 每次游戏暂停或者结束时，读取分数
        with open(filename, 'r', encoding='utf-8') as f:
            items = [line.strip() for line in f if line.strip()]
        return items

    def draw_font(self, game):
        # 每次游戏暂停或者结束时，显示游戏历史最高分、当前分数
        if not game.pause_switch:
            font = pygame.font.SysFont(None, 36)

            scores = self.read_score()

            current_score = font.render(f'score:{len(game.snake.bodies)}', True, (255, 255, 255))
            self.screen.blit(current_score, (10, 50))

            if scores:  # 确保列表不为空
                try:
                    # 转换为整数列表
                    int_scores = [int(s) for s in scores if s.isdigit()]
                    if int_scores:  # 确保转换后有数据
                        highest = max(int_scores)
                        all_time_high = font.render(f'highest score:{highest}', True, (255, 255, 255))
                    else:
                        all_time_high = font.render('highest score:0', True, (255, 255, 255))
                except ValueError:
                    # 如果有非数字内容，使用默认值
                    all_time_high = font.render('highest score:0', True, (255, 255, 255))
            else:
                all_time_high = font.render('highest score:0', True, (255, 255, 255))

            self.screen.blit(all_time_high, (10, 90))








