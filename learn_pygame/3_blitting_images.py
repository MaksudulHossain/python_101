import pygame 

#initilaize pygame
pygame.init()

# cratea  a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))    
pygame.display.set_caption("Blitting images")

# surface
# then rect 
dragon_left_image = pygame.image.load("dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0,0)

dragon_right_image =  pygame.image.load("dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)

running = True
while running:
    # loop through a list of events
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    #blit a  surface objcet
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)
    
    pygame.draw.line(display_surface, (255,255,255),(0,175),(WINDOW_WIDTH,175),5)
    #update display
    pygame.display.update()

pygame.quit()