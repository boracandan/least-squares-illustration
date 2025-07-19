import pygame

from settings import *
from grid import Grid

class LeastSquaresIllustration:
    def __init__(self) -> None:
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('LeastSquaresIllustration')
        self.clock = pygame.time.Clock()
        self.running = True

        # groups 
        self.all_sprites = pygame.sprite.Group()

        # Grid
        self.grid = Grid(WINDOW_WIDTH, WINDOW_HEIGHT)

        # Text 

        # Start game loop
        self.run()

    def run(self) -> None:
        while self.running:
            dt = self.clock.tick() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                self.grid.handle_event(event)

            # Update
            self.all_sprites.update()
            
            # Draw
            self.display_surface.fill("white")
            self.grid.draw()

            pygame.display.update()

            print(self.grid.unitSize)

        pygame.quit()


if __name__ == "__main__":
    LeastSquaresIllustration()