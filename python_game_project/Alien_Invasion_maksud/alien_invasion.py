import sys 
import pygame

class AlienInvasion:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):

        while True:
            for even in pygame.event.get():
                if even.type == pygame.QUIT:
                    sys.exit() 

            pygame.display.flip()

if __name__ == '__main':
    ai = AlienInvasion()
    ai.run_game()