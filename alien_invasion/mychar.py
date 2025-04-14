import pygame 
from settings import Settings

class MyChar:
    def __init__(self, screen):
        """init the char and set start position"""
        self.screen = screen

        # load the char and get its rect
        self.image = pygame.image.load('images/michel.bmp')
        self.image.set_colorkey(Settings().bg_color)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at bottom center of the scrren
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """Draw the char at current location"""
        self.screen.blit(self.image, self.rect)

    