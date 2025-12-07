class GameStates(object):
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.setting = ai_game.setting
        self.reset_states()
        self.high_score = 0
        self.level = 1

    def reset_states(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.setting.ship_limit
        self.score = 0
