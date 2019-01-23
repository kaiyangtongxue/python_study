import pygame
import time
from pygame.locals import *
import os
from plane import HeroPlane,EnemyPlane
'''
1、搭建主界面，完成主要窗口和背景图的显示
2、显示所有的内容
3、实现对玩家飞机的键盘监听和控制
'''

def key_control(hero):
    '''
    用来实现控制
    :param hero:用户飞机
    :return:
    '''
    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left_Down')
                hero.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                print('right_Down')
                hero.move_right()
            elif event.key == K_w or event.key == K_UP:
                print('up_Down')
                hero.move_up()
            elif event.key == K_s or event.key == K_DOWN:
                print('down_Down')
                hero.move_down()
            elif event.key == K_SPACE:
                print('space')
                hero.fire()
        elif event.type == KEYUP:
            if event.key == K_a or event.key == K_LEFT:
                print('left_Relase')
                hero.no_move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                print('right_Relase')
                hero.no_move_right()
            elif event.key == K_w or event.key == K_UP:
                print('up_Relase')
                hero.no_move_up()
            elif event.key == K_s or event.key == K_DOWN:
                print('down_Relase')
                hero.no_move_down()
            # elif event.key == K_SPACE:
            #     print('space')
            #     hero.no_fire()


def main():
    pygame.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50, 30)
    # 1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 780), 0, 32)
    # 6. 绘制分数
    # 加载字体
    textFont = pygame.font.SysFont("simkai.ttf", 30)
    # True = 抗锯齿
    # (255,255,255) = 使用白色绘制
    # 返回值textSurface = 返回要绘制的文字表面
    score = 0



    # 2. 创建一个和窗口大小一样的图片，用来当背景
    background = pygame.image.load("./feiji/background.png")
    # 4. 创建一个飞机图片
    hero = HeroPlane(screen)
    # 5. 创建敌机
    enemy = EnemyPlane(screen)
    # 3.把背景放到窗口中显示
    x = 200
    y = 630
    while True:
        # 设定需要显示的背景图
        screen.blit(background, (0, 0))
        # 绘制文字在(10,10)位置
        textSurface = textFont.render("Score:%d" % score, True, (255, 255, 255))
        screen.blit(textSurface, (10, 10))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()
        # 获取键盘事件，比如按键等
        key_control(hero)
        if hero.hit(enemy):
            score+=1
        enemy.hit(hero)
        # 更新需要显示的内容
        pygame.display.update()
        time.sleep(0.01)


if __name__ == "__main__":
    main()
