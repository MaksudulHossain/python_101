import pygame 

class Ship:
    def __init__(self, ai_settings, screen):
        """init the ship and set start pos"""
        self.screen = screen
        self.ai_settings = ai_settings
        # load the ship and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # movement flag
        self.moving_right = False
        self.moving_left = False

        # start each new ship at bottom center of the scrren
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # storeimal value for the ship's center
        self.center = float(self.rect.centerx)

    def update(self):
        """update the ship pos based on flag"""
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        # update the rect
        self.rect.centerx = self.center
    def blitme(self):
        """Draw the ship at current location"""
        self.screen.blit(self.image, self.rect)

    