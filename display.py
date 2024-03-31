import pygame as pg

class Display():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([500, 500])
        self.screen.fill((255, 255, 255))

        image = pg.image.load("icon.png")
        pg.display.set_icon(image)
        pg.display.set_caption("Cube")

    
    def draw_cube(self):
        pg.draw.polygon(self.screen, (200, 200, 200), [(250, 225), (100, 150), (250, 75), (400, 150)])
        pg.draw.polygon(self.screen, (100, 100, 100), [(250, 225), (250, 393), (100, 318), (100, 150)])
        pg.draw.polygon(self.screen, (150, 150, 150), [(250, 225), (250, 393), (400, 318), (400, 150)])
        pg.display.flip()