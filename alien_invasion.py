import sys  # this module is needed to exit game when player quits

import pygame   # this module contains functionality we need to make a game. 

class AlienInvasion:    # starts as a class called AlienInvasion
    """ overall class to manage game assets and behaviour """

    def __init__(self):
        """ Initialise the game, and create game resources """
        pygame.init()   # this function initialises the background settings                       that pygame needs to work properly

    self.screen = pygame.display.set_mode((1200, 800)) # this defines the games                                                      window size 1200 wide                                                       800 pixels high.                                                            assigned self.screen                                                        so this will be in all                                                      methods in the class
    pygame.display.set_caption("Alien Invasion")


def run_game(self):
    """ Start main loop for game """
    
    while True:
        # watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()



    # make the most recently drawn screen visible.
        pygame.display.flip()



if __name__ == '__main__':
    # make game instance and run game.
    ai = AlienInvasion()
    ai.run_game()


