import pygame.font


class Scoreboard(object):
    """显示得分信息的类"""

    def __init__(self, ai_game):
        """初始化显示得分涉及的属性"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setting = ai_game.setting
        self.states = ai_game.states

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 25)

        # 准备初始得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """将得分渲染成图像"""
        rounded_score = round(self.states.score, -1)
        score_str = f"score:{rounded_score:,}"
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.setting.bg_color
        )

        # 在屏幕右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """将最高分渲染为图像"""
        high_score = round(self.states.high_score, -1)
        high_score_str = f"HighScore:{high_score:,}"
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.setting.bg_color
        )

        # 将最高分放在屏幕的顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """将等级渲染成图像"""
        level_str = "level:" + str(self.states.level)
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.setting.bg_color
        )

        # 将等级放在等分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def check_high_score(self):
        """检查是否有最高分诞生"""
        if self.states.score > self.states.high_score:
            self.states.high_score = self.states.score
            self.prep_high_score()
