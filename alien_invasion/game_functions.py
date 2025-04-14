import sys
import pygame 

def check_events(ship):
    """Respond to mouse an dkeyboard"""
    for event in pygame.event.get():
        
            
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #move the ship to the right
                # ship.rect.centerx += 1
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                #move the ship to the right
                # ship.rect.centerx += 1
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_setting, screen, ship):
    """Update image on the screen and flip to new screen"""
    # redraw at each pass
    screen.fill(ai_setting.bg_color)
    ship.blitme()

    # make the most recent drawn screen visible
    pygame.display.flip()