# Alien Invasion

Python + Pygame 的横版射击练习项目，包含完整的事件循环、舰队生成、碰撞检测和记分板。

玩法
- 左右方向键移动飞船，空格射击，按 Q 退出。
- 点击屏幕中央的 Play 按钮开始或重新开始；失去全部飞船后游戏暂停并显示按钮。

核心功能
- 外星舰队整队移动，触边下落换向，触底或撞船会扣除飞船生命。
- 子弹命中外星人得分，清空一波后生成新舰队并提升速度（动态难度）。
- 记分板显示当前得分与历史最高分，并在超越时即时刷新。
- 所有静态/动态参数集中在 `setting.py`，便于调节速度、分值和子弹数量。

运行方式
- 环境：Python 3.9+，依赖 pygame。
- 可选：激活项目虚拟环境 `.\.venv\Scripts\activate`。
- 安装并运行：
  ```bash
  pip install pygame
  python alien_invasion.py
  ```

目录概览
- `alien_invasion.py`：入口与主循环、事件处理
- `setting.py`：屏幕/速度/分值等配置，含动态加速
- `ship.py`：飞船逻辑与重置
- `alien.py`：外星人模型与边缘检测
- `bullet.py`：子弹模型与绘制
- `game_states.py`：分数、生命等状态
- `scoreboard.py`：当前分/最高分渲染
- `button.py`：Play 按钮
- `images/`：位图资源（如 `ship.bmp`）

