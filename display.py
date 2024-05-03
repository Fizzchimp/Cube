import pygame as pg
import numpy as np

class Display():
    def __init__(self, width, height):
        pg.init()
        self.width, self.height = width, height
        self.screen = pg.display.set_mode([width, height])
        self.screen.fill((255, 255, 255))

        image = pg.image.load("01_icon.png")
        pg.display.set_icon(image)
        pg.display.set_caption("Cube")

        self.phase = 0

        # Centre co-ordinates
        self.x, self.y  = self.width / 2, self.height / 2

        # Length of side of cube
        self.length = self.width / 2.5 if self.width <= self.height else self.height / 2.5    


    def draw_cube(self):

        self.screen.fill((255, 255, 255))

        # Each vertex of hexagon
        cos30 = np.cos(np.pi / 6)
        phase = self.phase * np.pi / 180 + np.pi / 6
        x, y, length = self.x, self.y, self.length
        top, bottom = (x, y - length), (x, y + length)

        points = [(x + length * cos30 * np.sin(phase), y + length / 2 * (np.cos(phase) - 1)),
                  (x + length * cos30 * np.cos(phase), y + length / 2 * (-np.sin(phase) - 1)),
                  (x + length * cos30 * -np.sin(phase), y + length / 2 * (-np.cos(phase) - 1)),
                  (x + length * cos30 * -np.cos(phase), y + length / 2 * (np.sin(phase) - 1)),

                  (x + length * cos30 * np.sin(phase), y + length / 2 * (np.cos(phase) + 1)),
                  (x + length * cos30 * np.cos(phase), y + length / 2 * (-np.sin(phase) + 1)),
                  (x + length * cos30 * -np.sin(phase), y + length / 2 * (-np.cos(phase) + 1)),
                  (x + length * cos30 * -np.cos(phase), y + length / 2 * (np.sin(phase) + 1))]


        for i in range(4):
            pg.draw.line(self.screen, (100, 100, 100), points[i], points[i + 4])
        for i in range(3):
            pg.draw.line(self.screen, (100, 100, 100), points[i], points[i + 1])
            pg.draw.line(self.screen, (100, 100, 100), points[i + 4], points[i + 5])

        pg.draw.line(self.screen, (100, 100, 100), points[3], points[0])
        pg.draw.line(self.screen, (100, 100, 100), points[7], points[4])
        
       # shade1 = [int(100 * (1 + np.cos(phase))) for i in range(3)]
       # shade2 = [int(100 * (1 + np.sin(phase))) for i in range(3)]
       # pg.draw.polygon(self.screen, shade1, (points[0], points[1], points[5], points[4]))
       # pg.draw.polygon(self.screen, shade2, (points[0], points[4], points[7], points[3]))
       # pg.draw.polygon(self.screen, (200, 200, 200), points[0:4])
        
        
        if self.phase < 0: self.phase += 1
        if self.phase > 0: self.phase -= 1
        

def main():
    screen = Display(700, 700)
    running = True
    keyDown = False
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT: running = False
            if event.type == pg.KEYDOWN: keyDown, key = True, event.key
            if event.type == pg.KEYUP: keyDown = False

        if keyDown:
            if key == pg.K_ESCAPE: running = False
            if key == pg.K_RIGHT and screen.phase == 0: screen.phase = -90
            if key == pg.K_LEFT and screen.phase == 0: screen.phase = 90
  
        screen.draw_cube()
        pg.display.flip()
        pg.time.wait(2)
    pg.quit()

#main()
