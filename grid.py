import pygame

class Grid:
    def __init__(self, screenWidth: int, screenHeight: int) -> None:
        self.displaySurface = pygame.display.get_surface()

        self.width = screenWidth
        self.height = screenHeight

        self.scale = 50 # pixels between lines
        self.maxScale, self.minScale, self.defaultScale = 100, 25, 50
        self.scalingMultiplier = 3
        self.unitSize = 1.0 # World units per grid square
        self.origin = pygame.Vector2((int(screenWidth // 2), int(screenHeight // 2)))

        # Position UI
        self.font = pygame.font.Font(filename=None, size=20)
        self.roundDigits = 3

    def draw_ui(self) -> None:
        self.mousePosition = (pygame.Vector2(pygame.mouse.get_pos()) - pygame.Vector2(self.origin)) / self.scale * self.unitSize
        textSurf = self.font.render(f"x: {round(self.mousePosition.x, self.roundDigits)}, y: {round(-self.mousePosition.y, self.roundDigits)}", True, "black")
        textRect = textSurf.get_frect(topleft = (0, 0))

        self.displaySurface.blit(textSurf, textRect)

    def draw_horizontal_label(self, y: float) -> None:
        coordinate = (y - self.origin.y) / self.scale * self.unitSize
        label = round(-coordinate, self.roundDigits)
        labelStr = str(label)

        font_size = max(int(self.scale * 0.4 - len(labelStr)), 10)  # adjust as needed
        font = pygame.font.Font(filename=None, size=font_size)

        textSurf = font.render(str(label), True, "black")
        textRect = textSurf.get_frect(midright = (self.origin.x, y))
        self.displaySurface.blit(textSurf, textRect)

    def draw_vertical_label(self, x: float) -> None:
        coordinate = (x - self.origin.x) / self.scale * self.unitSize
        label = round(coordinate, self.roundDigits)
        labelStr = str(label)

        font_size = max(int(self.scale * 0.4 - len(labelStr)), 10)  # adjust as needed
        font = pygame.font.Font(filename=None, size=font_size)

        textSurf = font.render(str(label), True, "black", )
        textRect = textSurf.get_frect(midtop = (x, self.origin.y))
        self.displaySurface.blit(textSurf, textRect)

    def draw_axis(self) -> None:
        # Draw Grid
        for xPos in range(int(self.origin.x) + int(self.scale), self.width, int(self.scale)):
            pygame.draw.line(self.displaySurface, "#b7b8b4", (xPos, 0), (xPos, self.height))

            self.draw_vertical_label(xPos)

        for xPos in range(int(self.origin.x) - int(self.scale), 0, -int(self.scale)):
            pygame.draw.line(self.displaySurface, "#b7b8b4", (xPos, 0), (xPos, self.height))

            self.draw_vertical_label(xPos)

        for yPos in range(int(self.origin.y) + int(self.scale), self.height, int(self.scale)):
            pygame.draw.line(self.displaySurface, "#b7b8b4", (0, yPos), (self.width, yPos))

            self.draw_horizontal_label(yPos)
        
        for yPos in range(int(self.origin.y) - int(self.scale), 0, -int(self.scale)):
            pygame.draw.line(self.displaySurface, "#b7b8b4", (0, yPos), (self.width, yPos))

            self.draw_horizontal_label(yPos)

            
        # Draw Axis Lines
        pygame.draw.line(self.displaySurface, "black", (self.origin.x, 0), (self.origin.x, self.height))
        pygame.draw.line(self.displaySurface, "black", (0, self.origin.y), (self.width, self.origin.y))


    def update_scale(self) -> None:
        if self.minScale <= self.scale <= self.maxScale:
            return
        self.unitSize *= self.defaultScale / self.maxScale if self.scale > self.maxScale else self.defaultScale / self.minScale
        self.scale = self.defaultScale

    def draw(self) -> None:
        self.draw_axis()
        self.draw_ui()
    
    def handle_event(self, event: pygame.Event) -> None:
        if event.type == pygame.MOUSEWHEEL:
            mouseScreen = pygame.Vector2(pygame.mouse.get_pos())
            preMousePosition = (mouseScreen - self.origin) / self.scale * self.unitSize
            self.scale += event.y * self.scalingMultiplier
            self.update_scale()
            newMousePosition = (mouseScreen - self.origin) / self.scale * self.unitSize
            self.adjust_origin(preMousePosition, newMousePosition)
    
    def adjust_origin(self, preMousePos: pygame.Vector2, newMousePos: pygame.Vector2) -> None:
        offset = newMousePos - preMousePos
        pixel_offset = offset / self.unitSize * self.scale
        self.origin += pygame.Vector2(round(pixel_offset.x), round(pixel_offset.y))



