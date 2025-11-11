import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理飞船所发射的子弹"""

    def __init__(self, ai_game):
        """在飞船当前位置创建一个子弹对象"""
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.color = ai_game.setting.bullet_color

        # 在(0,0)处设置一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(
            0, 0, self.setting.bullet_width, self.setting.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        # 存储用浮点数表示子弹位置
        self.y = float(self.rect.y)

    def update(self):
        """向上更新子弹"""
        # 更新子弹的准确位置
        self.y -= self.setting.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
