class Settings():
    """存储《外星人入侵》的所有的设置的类"""

    def __init__(self):
        """ 初始化游戏的设置 """
        # 屏幕设置
        self.screen_width = 1200
        self.screen_hight = 600
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        # 飞船的移动像素为1.5一次
        self.ship_speed_factor = 1.5

