import pygame

class Base(object):
    def __init__(self, screen_temp, x, y, image):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.live = True
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        self.rect.x=self.x
        self.rect.y=self.y