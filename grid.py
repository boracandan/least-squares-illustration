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

        self.preMousePosition = pygame.Vector2(pygame.mouse.get_pos())

        self.points = []



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
            if xPos >= 0:
                pygame.draw.line(self.displaySurface, "#b7b8b4", (xPos, 0), (xPos, self.height))

                self.draw_vertical_label(xPos)

        for xPos in range(int(self.origin.x) - int(self.scale), 0, -int(self.scale)):
            if xPos <= self.width:
                pygame.draw.line(self.displaySurface, "#b7b8b4", (xPos, 0), (xPos, self.height))

                self.draw_vertical_label(xPos)

        for yPos in range(int(self.origin.y) + int(self.scale), self.height, int(self.scale)):
            if yPos >= 0:
                pygame.draw.line(self.displaySurface, "#b7b8b4", (0, yPos), (self.width, yPos))

                self.draw_horizontal_label(yPos)
        
        for yPos in range(int(self.origin.y) - int(self.scale), 0, -int(self.scale)):
            if yPos <= self.height:
                pygame.draw.line(self.displaySurface, "#b7b8b4", (0, yPos), (self.width, yPos))

                self.draw_horizontal_label(yPos)

            
        # Draw Axis Lines
        pygame.draw.line(self.displaySurface, "black", (self.origin.x, 0), (self.origin.x, self.height))
        pygame.draw.line(self.displaySurface, "black", (0, self.origin.y), (self.width, self.origin.y))

    def draw_points(self) -> None:
        pointWorldCoordinates = list(map(lambda point: self.origin + point / self.unitSize * self.scale, self.points))
        for pointCoordinate in pointWorldCoordinates:
            if 0 < pointCoordinate.y < self.height and 0 < pointCoordinate.x < self.width:
                pygame.draw.circle(self.displaySurface, "purple", pointCoordinate, 4)

    def update_scale(self) -> None:
        if self.minScale <= self.scale <= self.maxScale:
            return
        self.unitSize *= self.defaultScale / self.maxScale if self.scale > self.maxScale else self.defaultScale / self.minScale
        self.scale = self.defaultScale

    def draw(self) -> None:
        self.draw_axis()
        self.draw_ui()
        self.draw_points()
    
    def handle_event(self, event: pygame.Event) -> None:
        if event.type == pygame.MOUSEWHEEL:
            mouseScreen = pygame.Vector2(pygame.mouse.get_pos())
            preMousePosition = (mouseScreen - self.origin) / self.scale * self.unitSize
            self.scale += event.y * self.scalingMultiplier
            self.update_scale()
            newMousePosition = (mouseScreen - self.origin) / self.scale * self.unitSize
            self.adjust_origin(preMousePosition, newMousePosition)
        
    def update(self) -> None:
        mousePressed = pygame.mouse.get_pressed()
        mouseJustPressed = pygame.mouse.get_just_pressed()
        self.handle_mouse_drag(mousePressed)
        self.handle_mouse_just_pressed(mouseJustPressed)

    def adjust_origin(self, preMousePos: pygame.Vector2, newMousePos: pygame.Vector2) -> None:
        offset = newMousePos - preMousePos
        pixel_offset = offset / self.unitSize * self.scale
        self.origin += pygame.Vector2(round(pixel_offset.x), round(pixel_offset.y))

    def handle_mouse_drag(self, mousePressed: list) -> None:
        mousePos = pygame.Vector2(pygame.mouse.get_pos())
        if mousePressed[0]: # Mouse Left Click
            self.origin += mousePos - self.preMousePosition
        self.preMousePosition = mousePos

    def handle_mouse_just_pressed(self, mouseJustPressed: list) -> None:
        if mouseJustPressed[2]: # Mouse Right Click
            mousePos = (pygame.Vector2(pygame.mouse.get_pos()) - self.origin) / self.scale * self.unitSize
            self.points.append(mousePos)
