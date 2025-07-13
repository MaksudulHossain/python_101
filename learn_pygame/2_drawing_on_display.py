import pygame 

# initilaize pygame 
pygame.init()

# create  a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing objects")

# define colors as rgb 
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)

display_surface.fill(BLUE)

# draw various shapes 
# Line(surface, color, starting point, ending point, thickness)
pygame.draw.line(display_surface, RED, (0,0), (100,100), 5)
pygame.draw.line(display_surface, YELLOW, (100,100), (200,300), 1)

# circle(surface, color, center, radius, thickness, 0 for fill)
pygame.draw.circle(display_surface, WHITE, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 200, 6)
pygame.draw.circle(display_surface, YELLOW, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 195, 0)

#rect
# rect(surface, color, rect, thickness)
pygame.draw.rect(display_surface, CYAN, (50, 50, 100, 100), 0)
pygame.draw.rect(display_surface, MAGENTA, (200, 50, 100, 100), 5)

# the main game loop
running = True 
while running:
    #loop through a list events
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    # update the display 
    pygame.display.update()

#end the game 
pygame.quit()

