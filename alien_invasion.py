import sys
import pygame
from setting import Setting
from ship import Ship


class AlienInvasion(object):
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        # 初始化时钟计时
        self.clock = pygame.time.Clock()
        # 初始化设置
        self.setting = Setting()

        # 设置背景色
        self.bg_color = (230, 230, 230)

        self.screen = pygame.display.set_mode(
            (self.setting.screen_width, self.setting.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._chek_events()
            self._update_screen()
            self.clock.tick(60)  # 帧速率

    def _chek_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        # 每次循环都重新绘制屏幕
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()

        pygame.display.flip()  # 让最近绘制的屏幕可见


if __name__ == "__main__":
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
