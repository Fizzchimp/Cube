import pygame as pg
import numpy as np

class Display():
    def __init__(self, width, height):
        pg.init()
        self.width, self.height = width, height
        self.screen = pg.display.set_mode([width, height])
        self.screen.fill((255, 255, 255))

        image = pg.image.load("icon.png")
        pg.display.set_icon(image)
        pg.display.set_caption("Cube")

        self.phase = 0

        # Centre co-ordinates
        self.x, self.y  = self.width / 2, self.height / 2

        # Length of side of cube
        self.z = self.width / 2.5 if self.width <= self.height else self.height / 2.5

    def draw_cube(self, rotating = False):

        self.screen.fill((255, 255, 255))


        # Each vertex of hexagon
        cos30 = np.cos(np.pi / 6)
        top, bottom = (self.x, self.y - self.z), (self.x, self.y + self.z)
        points = [(self.x - self.z * cos30, self.y - self.z * 0.5), (self.x + self.z * cos30, self.y - self.z * 0.5),
                  (self.x + self.z * cos30, self.y + self.z * 0.5), (self.x - self.z * cos30, self.y + self.z * 0.5)]
        
        colour1 = 150 + 50 * np.sin(self.phase)
        pg.draw.polygon(self.screen, (colour1, colour1, colour1), [(self.x, self.y), points[0], top, points[1]])

        colour2 = 150 + 50 * np.sin(self.phase + 2 * np.pi / 3)
        pg.draw.polygon(self.screen, (colour2, colour2, colour2), [(self.x, self.y), points[1], points[2], bottom])

        colour3 = 150 + 50 * np.sin(self.phase + 4 * np.pi / 3)
        pg.draw.polygon(self.screen, (colour3, colour3, colour3), [(self.x, self.y), bottom, points[3], points[0]])


        pg.display.flip()
        if rotating: self.phase += np.pi / 72



screen = Display(700, 700)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE): running = False

    screen.draw_cube(True)
    pg.time.wait(50)
pg.quit()