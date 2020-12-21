import pygame

class Ship:
    """ A class to manage the ship """

    def __init__(self, ai_game):
        """ Initialize ship and set its starting position """

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the ship and get its rect
        self.image = pygame.image.load('images/357-3576984_spaceship-cartoon-clipart.png')

        self.rect = self.image.get_rect()
        
        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the ships horizontal position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Update the ships position based on the movement flags """
        #Update ships x value, not the rekt
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed


    def blitme(self):
        """ Draw the ship at tits current location """

        self.screen.blit(self.image, self.rect)    
