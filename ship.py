import pygame


class Ship(object):
    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取取外接矩形
        self.image = pygame.image.load("images/ship.bmp").convert_alpha()
        self.image = pygame.transform.smoothscale(
            self.image, (80, 80)
        )  # 宽 80、高 120，可按需求修改
        self.rect = self.image.get_rect()

        # 每个新飞船都在底部中央
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
