import pygame

import game_functions as gf
from settings import Settings
from mychar import MyChar


def run_game():
    #init game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
        )
    pygame.display.set_caption("Alien Invasion")

    # make a ship
    michel = MyChar(screen)

    # start the main loop
    while True:

        # watch keyboard and mouse evenst
        gf.check_events()
        gf.update_screen(ai_settings, screen, michel)
        
        # make most reently drawn screen visible
        pygame.display.flip()

run_game()
            

