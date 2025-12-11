class Settings:
    def __init__(self):
        # 游戏设置类，存储所有可配置参数

        # 屏幕设置
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (0, 0, 0)  # 黑色背景

        # 蛇的设置
        self.snake_width = 20
        self.snake_height = 20
        self.snake_color = (67, 163, 239)  # 浅蓝色
        self.snake_speed = self.snake_width  # 移动速度等于蛇身宽度

        # 食物的设置
        self.food_width = 20
        self.food_height = 20
        self.food_color = (239, 118, 123)  # 浅红色

        # 按钮位置设置
        self.pause_button_x = 870  # 暂停按钮X坐标（右上角）
        self.pause_button_y = 30  # 暂停按钮Y坐标

        self.replay_button_x = 800  # 重玩按钮X坐标
        self.replay_button_y = 30  # 重玩按钮Y坐标

        self.pause1_button_x = 450  # 暂停界面大按钮X坐标（居中）
        self.pause1_button_y = 300  # 暂停界面大按钮Y坐标