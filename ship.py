import pygame


class Ship(object):
    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.get_rect()

        # 加载飞船图像并获取取外接矩形
        self.image = pygame.image.load("image/ship,,bmp")
        self.rect = self.image.get_rect()

        # 每个新飞船都在底部中央
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.iamge, self.rect)
