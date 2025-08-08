import pygame
import pygame_gui

from settings import *
from grid import Grid
from ui import RegressionUI

class LeastSquaresIllustration:
    def __init__(self) -> None:
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('LeastSquaresIllustration')
        self.clock = pygame.time.Clock()
        self.running = True

        # groups 
        self.all_sprites = pygame.sprite.Group()

        # UI
        self.uiManager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.ui = RegressionUI(pygame.Rect((WINDOW_WIDTH - 158, -2), (160, 120)), self.uiManager)

        # Grid
        self.grid = Grid(WINDOW_WIDTH, WINDOW_HEIGHT, ui=self.ui)

        # Start game loop
        self.run()

    def run(self) -> None:
        while self.running:
            dt = self.clock.tick() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                self.grid.handle_event(event)

                self.uiManager.process_events(event)

            # Update
            self.uiManager.update(dt)
            self.all_sprites.update()
            self.grid.update()
            
            # Draw
            self.display_surface.fill("white")
            self.grid.draw()
            self.uiManager.draw_ui(self.display_surface)

            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    LeastSquaresIllustration()