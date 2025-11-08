class Setting(object):
    """存储游戏alien invasion中的设置"""

    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        
        # 飞船的设置
        self.ship_speed=1.5
