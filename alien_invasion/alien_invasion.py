import sys  

import pygame    

from settings import Settings


class AlienInvasion:    
    """ overall class to manage game assets and behaviour """

    def __init__(self):
        """ Initialise the game, and create game resources """
        pygame.init()
        self.settings = Settings() 

    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 


    pygame.display.set_caption("Alien Invasion")

    # set background colour
    self.bg_color = (230, 230, 230)


def run_game(self):
    """ Start main loop for game """
    
    while True:
        # watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    # redraw the screen during each pass of the loop (start a new game)
        self.screen.fill(self.settings.bg_color)        



    # make the most recently drawn screen visible.
        pygame.display.flip()



if __name__ == '__main__':
    # make game instance and run game.
    ai = AlienInvasion()
    ai.run_game()


