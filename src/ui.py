import pygame_gui
import pygame

from settings import *

class RegressionUI:
    def __init__(self, rect: pygame.Rect, manager: pygame_gui.UIManager) -> None:
        # --- Simple Regress UI Panel ---
        self.uiPanel = pygame_gui.elements.UIPanel(
            relative_rect=rect, 
            manager=manager
        )

        # Label "n ="
        self.nLabel = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((10, 10), (30, 30)),
            text="n =",
            manager=manager,
            container=self.uiPanel
        )

        # Input box for n
        self.nInput = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((45, 10), (100, 30)),
            manager=manager,
            container=self.uiPanel
        )
        self.nInput.set_text("1")  # Default value

        # Regress button
        self.regressButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((10, 60), (135, 40)),
            text="Regress",
            manager=manager,
            container=self.uiPanel
        )
    
    @property
    def mouseInPanel(self) -> bool:
        mousePos = pygame.mouse.get_pos()
        panelRect = self.uiPanel.get_abs_rect()

        return panelRect.collidepoint(mousePos)