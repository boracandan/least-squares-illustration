import pygame

from settings import *

class LeastSquaresIllustration:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('LeastSquaresIllustration')
        self.clock = pygame.time.Clock()
        self.running = True

        # groups 
        self.all_sprites = pygame.sprite.Group()


        # Start game loop
        self.run()

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Update
            self.all_sprites.update()
            
            # Draw
            self.display_surface.fill("blue")
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    LeastSquaresIllustration()