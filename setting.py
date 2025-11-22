class Setting(object):
    """存储游戏alien invasion中的设置"""

    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 6

        # 外星人设置
        self.alien_speed = 1.5
        self.fleet_drop_speed = 20
        # fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1
