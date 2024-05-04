import pygame as pg
import numpy as np
COS30 = np.cos(np.pi / 6)
THRDPI = np.pi / 3


class Display():
    def __init__(self, width, height):
        pg.init()
        self.width, self.height = width, height
        self.screen = pg.display.set_mode([width, height])
        self.screen.fill((255, 255, 255))

        image = pg.image.load("01_icon.png")
        pg.display.set_icon(image)
        pg.display.set_caption("Cube")

        self.xPhase = 0
        self.yPhase = 0

        # Centre co-ordinates
        self.x, self.y  = self.width / 2, self.height / 2

        # Length of side of cube
        self.length = self.width / 2.5 if self.width <= self.height else self.height / 2.5    


    def draw_cube(self):

        self.screen.fill((255, 255, 255))

        # Each vertex of hexagon
        xPhase = self.xPhase * np.pi / 180 + np.pi / 6
        yPhase = self.yPhase * np.pi / 180# + np.pi / 6
        x, y, length = self.x, self.y, self.length
        top, bottom = (x, y - length), (x, y + length)

        points = [(x + length * COS30 * np.sin(yPhase), y + length / 2 * (np.cos(yPhase) - 1)),
                 (x + length * COS30 * np.cos(yPhase), y + length / 2 * (-np.sin(yPhase) - 1)),
                 (x + length * COS30 * -np.sin(yPhase), y + length / 2 * (-np.cos(yPhase) - 1)),
                 (x + length * COS30 * -np.cos(yPhase), y + length / 2 * (np.sin(yPhase) - 1)),

                 (x + length * COS30 * np.sin(yPhase), y + length / 2 * (np.cos(yPhase) + 1)),
                 (x + length * COS30 * np.cos(yPhase), y + length / 2 * (-np.sin(yPhase) + 1)),
                 (x + length * COS30 * -np.sin(yPhase), y + length / 2 * (-np.cos(yPhase) + 1)),
                 (x + length * COS30 * -np.cos(yPhase), y + length / 2 * (np.sin(yPhase) + 1))]
    
        
        newPoints = [(x + length * COS30 / 2 + length / 2 * np.sin(xPhase), y + length / 4 + 3 * length / 4 * np.cos(xPhase)),
                  (x + length * COS30 / 2 + length / 2 * -np.cos(xPhase), y + length / 4 + 3 * length / 4 * np.sin(xPhase)),
                  (x + length * COS30 / 2 + length / 2 * -np.sin(xPhase), y + length / 4 + 3 * length / 4 * -np.cos(xPhase)),
                  (x + length * COS30 / 2 + length / 2 * np.cos(xPhase), y + length / 4 + 3 * length / 4 * -np.sin(xPhase)),

                  (x - length * COS30 / 2 + length / 2 * np.sin(xPhase), y - length / 4 + 3 * length / 4 * np.cos(xPhase)),
                  (x - length * COS30 / 2 + length / 2 * -np.cos(xPhase), y - length / 4 + 3 * length / 4 * np.sin(xPhase)),
                  (x - length * COS30 / 2 + length / 2 * -np.sin(xPhase), y - length / 4 + 3 * length / 4 * -np.cos(xPhase)),
                  (x - length * COS30 / 2 + length / 2 * np.cos(xPhase), y - length / 4 + 3 * length / 4 * -np.sin(xPhase))]



        for i in range(4):
            pg.draw.line(self.screen, (100, 100, 100), points[i], points[i + 4])
        for i in range(3):
            pg.draw.line(self.screen, (255, 100, 100), points[i], points[i + 1])
            pg.draw.line(self.screen, (100, 100, 255), points[i + 4], points[i + 5])

        pg.draw.line(self.screen, (255, 100, 100), points[3], points[0])
        pg.draw.line(self.screen, (100, 100, 255), points[7], points[4])
        
        for i in range(4):
            pg.draw.line(self.screen, (100, 100, 100), newPoints[i], newPoints[i + 4])
        for i in range(3):
            pg.draw.line(self.screen, (255, 100, 100), newPoints[i], newPoints[i + 1])
            pg.draw.line(self.screen, (100, 100, 255), newPoints[i + 4], newPoints[i + 5])

        pg.draw.line(self.screen, (255, 100, 100), newPoints[3], newPoints[0])
        pg.draw.line(self.screen, (100, 100, 255), newPoints[7], newPoints[4])
        
        
        if self.yPhase < 0: self.yPhase += 1
        if self.yPhase > 0: self.yPhase -= 1
        if self.xPhase < 0: self.xPhase += 1
        if self.xPhase > 0: self.xPhase -= 1
        

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
            if key == pg.K_RIGHT and screen.yPhase == 0: screen.yPhase = -90
            if key == pg.K_LEFT and screen.yPhase == 0: screen.yPhase = 90
            if key == pg.K_DOWN and screen.xPhase == 0: screen.xPhase = -90
            if key == pg.K_UP and screen.xPhase == 0: screen.xPhase = 90
  
        screen.draw_cube()
        pg.display.flip()
        pg.time.wait(20)
    pg.quit()

main()
