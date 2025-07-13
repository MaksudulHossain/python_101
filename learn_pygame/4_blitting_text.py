import pygame
pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("setting images")

# define colors as rgb 
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)

# see all sys fonts 
fonts = pygame.font.get_fonts()

for font in fonts:
    print(font)


# define fomnt 
system_font = pygame.font.SysFont('calibri', 64)
custom_font = pygame.font.Font('aAttackGraffiti.ttf', 32)

system_text = system_font.render("Dragons rule", True, RED, WHITE)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

custom_text = custom_font.render("Move the dragon soon", True, RED, WHITE)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100)


running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)

    pygame.display.update()

pygame.quit()