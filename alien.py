import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人"""

    def __init__(self, ai_game):
        """初始化外星人并设置其初始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting

        # 加载外星人图像并设置rect属性
        self.image = pygame.image.load("images/alien.bmp").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (50, 60))
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确水平位置
        self.x = float(self.rect.x)

    def check_edges(self):
        """如果外星人位于屏幕边缘,就返回true"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self, *args, **kwargs):
        """向左或向右移动外星人"""
        self.x += self.setting.alien_speed * self.setting.fleet_direction
        self.rect.x = self.x
