from base import  Base
import pygame
from direction import Direction
from bullet import Bullet,EnemyBullet
import random
speed = 5

class BasePlane(Base):
    '''
    飞机基类
    '''

    def __init__(self, screen_temp, x, y, image_name):
        Base.__init__(self, screen_temp, x, y, image_name)
        self.bullet_list = []

    def display(self):
        Base.display(self)
        del_list = list()
        # 删除越界子弹
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge()or bullet.live==False:
                del_list.append(bullet)
        for bullet in del_list:
            self.bullet_list.remove(bullet)

    def hit(self,enemy):
        for bullet in self.bullet_list:
            if bullet.hit(enemy):
                bullet.live=False
                enemy.live=False
                return True

class HeroPlane(BasePlane):
    '''
    玩家的飞机类
    '''

    def __init__(self, screen_temp):
        image = pygame.image.load("./feiji/hero1.png")
        BasePlane.__init__(
            self,
            screen_temp,
            240 -
            image.get_rect().width /
            2,
            630,
            "./feiji/hero1.png")
        self.dir = Direction()

    def display(self):
        BasePlane.display(self)
        self.move()

    def move(self):
        '''
        用来根据方向来更新玩家的飞机位置
        :return:
        '''
        if(self.dir.getleft()):
            self.x -= speed
            print('left')
        if (self.dir.getright()):
            self.x += speed
            print('right')
        if (self.dir.getup()):
            self.y -= speed
            print('up')
        if (self.dir.getdown()):
            self.y += speed
            print('down')
    # 根据键盘输入来更新方向

    def move_left(self):
        self.dir.setleft(True)

    def move_right(self):
        self.dir.setright(True)

    def move_up(self):
        self.dir.setup(True)

    def move_down(self):
        self.dir.setdown(True)

    def no_move_left(self):
        self.dir.setleft(False)

    def no_move_right(self):
        self.dir.setright(False)

    def no_move_up(self):
        self.dir.setup(False)

    def no_move_down(self):
        self.dir.setdown(False)

    def fire(self):
        self.bullet_list.append(
            Bullet(
                self.screen,
                (self.x +
                 self.image.get_rect().width /
                 2 -
                 10),
                (self.y +
                 5)))


class EnemyPlane(BasePlane):
    '''
    敌机类
    '''

    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 0, 0, "./feiji/enemy0.png")
        self.flag = 1

    def move(self):
        self.x += speed * self.flag
        if self.x > 480 - self.image.get_rect().width or self.x < 0:
            self.flag = -1 * self.flag

    def fire(self):
        random_num = random.randint(1, 100)
        if random_num == 58 or random_num == 78:
            self.bullet_list.append(
                EnemyBullet(
                    self.screen,
                    self.x +
                    self.image.get_rect().width /
                    2 -
                    5,
                    self.y +
                    self.image.get_rect().height))
