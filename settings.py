class Settings():
    """存储《外星人入侵》的所有的设置的类"""

    def __init__(self):
        """ 初始化游戏的设置 """
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船的设置

        # 一开始玩家拥有的飞船数量,从0开始计数
        self.ship_limit = 0

        # 子弹的设置
        self.bullet_width = 300
        self.bullet_hight = 15
        self.bullet_color = 60, 60, 60
        # 子弹的数量
        self.bullets_allowed = 300

        # 外星人的设置
        self.fleet_drop_speed = 20

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化游戏进行而变化的设置"""
        # 飞船的移动像素为1.5一次
        self.ship_speed_factor = 1.5
        # 子道的移动像素为3一次
        self.bullet_speed_factor = 3
        # 外星人的移动像素为1一次
        self.alien_speed_factor = 1

        # fleet_direction 为 1 表示向右移，为-1表示向左移
        self.fleet_direction = 1

        # 计分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置和外星人点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

