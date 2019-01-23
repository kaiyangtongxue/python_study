import pygame

'''
一切对象的基类
'''
class Base(object):
    def __init__(self, screen_temp, x, y, image):
        '''
        初始化函数
        :param screen_temp: 屏幕
        :param x: 图片的x位置
        :param y: 图片的y位置
        :param image: 图片的地址
        '''
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.live = True
    def display(self):
        '''
        绘制函数
        :return:
        '''
        self.screen.blit(self.image, (self.x, self.y))
        self.rect.x=self.x
        self.rect.y=self.y
    def getrect(self):
        '''
        返回矩形的位置和长宽，便于做碰撞检测
        :return:
        '''
        return self.rect