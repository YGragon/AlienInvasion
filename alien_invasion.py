import sys
import pygame
import game_functions as gf


from settings import Settings
from ship import Ship


def run_game():
    # 初始化游戏并创建屏幕对象
    pygame.init()
    ai_settings = Settings() ;
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_hight))

    pygame.display.set_caption("Alien Invasion")

    # 在屏幕上创建飞船
    ship = Ship(ai_settings, screen)

    # 设置背景色
    bg_color = (ai_settings.bg_color)

    # 开始游戏的主要循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(ship)
        # 刷新飞船的位置
        ship.update()
        # 刷新屏幕
        gf.update_screen(ai_settings, screen, ship)

run_game()
