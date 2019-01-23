from base import Base
import pygame


class Basebullet(Base):
    def __init__(self, screen_temp, x, y, image_name):
        Base.__init__(self, screen_temp, x, y, image_name)

    def hit(self,enemy):
        if pygame.Rect.colliderect(self.getrect(),enemy.getrect()):
            print('hit')
            return True
        else:
            return False


class Bullet(Basebullet):
    '''
    子弹类，用来表示子弹信息
    '''

    def __init__(self, screen_temp, x, y):
        Basebullet.__init__(self, screen_temp, x, y, "./feiji/bullet.png")

    def move(self):
        self.y -= 5

    def judge(self):
        if self.y < -5:
            return True
        else:
            return False


class EnemyBullet(Basebullet):
    '''
        子弹类，用来表示飞机信息
    '''

    def __init__(self, screen_temp, x, y):
        Basebullet.__init__(self, screen_temp, x, y, "./feiji/bullet1.png")

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 800:
            return True
        else:
            return False
