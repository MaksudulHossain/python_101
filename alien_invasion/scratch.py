import pygame

pygame.init()

image = pygame.image.load("images/ship.bmp")
width, height = image.get_size()

print(f"Image size: width={width} height={height}")