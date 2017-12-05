import game_functions as gf

class GameStats(object):
    """跟踪游戏的统计信息"""
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏刚启动时处于非活动状态
        self.game_active = False

        # 在任何情况下都不应该重置最高分
        # 先从文件中读取，有则显示最高分，没有则显示0
        read_high_score = gf.read_high_score()
        print(read_high_score)
        if read_high_score.strip() == '':
            print(read_high_score+"为空")
            self.high_score = int(0)
        else:
            self.high_score = int(read_high_score)
            print(str(self.high_score)+"==最终结果")


    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        # 玩家等级
        self.level = 1

