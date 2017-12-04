class Settings():
    """存储《外星人入侵》的所有的设置的类"""

    def __init__(self):
        """ 初始化游戏的设置 """
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        # 飞船的移动像素为1.5一次
        self.ship_speed_factor = 1.5
        # 一开始玩家拥有的飞船数量,从0开始计数
        self.ship_limit = 2

        # 子弹的设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_hight = 15
        self.bullet_color = 60, 60, 60
        # 子弹的数量
        self.bullets_allowed = 3

        # 外星人的设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction 为 1 表示向右移，为-1表示向左移
        self.fleet_direction = 1

