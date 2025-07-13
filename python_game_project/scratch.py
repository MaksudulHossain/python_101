import pygame

class Main:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(size=(800,600))
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        x = 100
        y = 100
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            
            self.screen.fill((0,255,0))
            pygame.draw.rect(self.screen, (255,0,0),(x,y,100,100))

            x += 1
            y += 1
            pygame.display.flip()

main = Main()
main.run_game()