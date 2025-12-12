import pygame
import settings
from snake import Snake
from food import Food
from pause_button import Pause
from replay_button import Replay
from pause_button_1 import Pause1


class Game:
    def __init__(self):
        # 初始化游戏主类
        pygame.init()  # 初始化pygame
        self.setting = settings.Settings()  # 加载游戏设置
        # 创建游戏窗口
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        self.screen_rect = self.screen.get_rect()  # 获取屏幕矩形区域
        pygame.display.set_caption("贪吃蛇2")  # 设置窗口标题

        icon = pygame.image.load('窗口图标.png')  # 创建窗口图标
        pygame.display.set_icon(icon)  # 更改窗口图标

        self.bg_color = self.setting.bg_color  # 背景颜色
        self.clock = pygame.time.Clock()  # 游戏时钟，控制帧率
        self.running = True  # 游戏运行状态
        self.pause_switch = True  # 暂停开关，True表示游戏进行中，False表示暂停

        # 创建自定义事件：蛇的移动事件
        self.move_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.move_event, 120)  # 每120毫秒触发一次

        # 初始化游戏对象
        self.snake = Snake(self)
        self.food = Food(self)
        self.pause = Pause(self)
        self.replay = Replay(self)
        self.pause1 = Pause1(self)

    def event_track(self):
        # 事件处理函数
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 处理退出事件
                self.running = False

            elif event.type == self.move_event and self.pause_switch:
                # 定时移动事件：如果游戏未暂停，则移动蛇
                self.snake.move(self)

            elif event.type == pygame.KEYDOWN:
                # 键盘按键事件
                if event.key == pygame.K_SPACE:
                    # 空格键：切换暂停状态
                    self.toggle_pause()
                elif event.key == pygame.K_UP:
                    self.snake.change_direction('up')
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction('down')
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction('right')
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction('left')

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 鼠标点击事件
                if self.pause.rect.collidepoint(event.pos):
                    # 点击暂停按钮
                    self.pause_switch = False
                elif self.pause1.rect.collidepoint(event.pos):
                    # 点击继续按钮（暂停界面的大按钮）
                    self.pause_switch = True
                elif self.replay.rect.collidepoint(event.pos):
                    self.replay.reset_parameters(self)

    def toggle_pause(self):
        # 切换暂停状态
        self.pause_switch = not self.pause_switch

    def collide_detection(self):
        # 碰撞检测：检测蛇是否吃到食物
        if self.food.crash_test(self.snake):
            # 如果吃到食物
            self.food.randomize_position(self.snake)  # 随机生成新食物位置
            self.food.is_eaten = False  # 重置食物状态
            self.snake.crash_test()  # 蛇增长

    def draw_screen(self):
        # 绘制游戏画面
        self.screen.fill(self.bg_color)  # 填充背景色
        self.snake.draw_snake()  # 绘制蛇
        self.food.draw_food()  # 绘制食物
        self.pause.draw()  # 绘制暂停按钮
        self.replay.draw()  # 绘制重玩按钮
        self.pause1.draw(self)  # 绘制暂停界面的大按钮（仅在暂停时显示）

    def run_game(self):
        # 游戏主循环
        while self.running:
            self.event_track()  # 处理事件
            self.collide_detection()  # 碰撞检测
            self.draw_screen()  # 绘制画面
            pygame.display.flip()  # 更新显示
            self.clock.tick(60)  # 控制帧率为60FPS


if __name__ == "__main__":
    # 程序入口点
    game = Game()
    game.run_game()
