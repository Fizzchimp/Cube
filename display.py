import pygame as pg
import numpy as np
COS30 = np.cos(np.pi / 6)
THRDPI = np.pi / 3
angle = 0

class CubePoints:
    def __init__(self, length):
        # self.points = [
        #     [length, length, length],
        #     [length, length, -length],
        #     [-length, length, -length],
        #     [-length, length, length],

        #     [length, -length, length],
        #     [length, -length, -length],
        #     [-length, -length, -length],
        #     [-length, -length, length]]
        
        self.points = [
            [length, length, -length, -length, length, length, -length, -length],
            [length, length, length, length, -length, -length, -length, -length],
            [length, -length, -length, length, length, -length, -length, length]]
        
    def rotateX(self, angle):
        angle = angle / 180 * np.pi
        rotX = [[1, 0, 0],
                [0, np.cos(angle), -np.sin(angle)],
                [0, np.sin(angle), np.cos(angle)]]
        return np.matmul(rotX, self.points)
        
    def rotateY(self, angle):
        angle = angle / 180 * np.pi
        rotY = [[np.cos(angle), 0, np.sin(angle)],
                [0, 1, 0],
                [-np.sin(angle), 0, np.cos(angle)]]
        
        return np.matmul(rotY, self.points)
    
    def rotateZ(self, angle):
        angle = angle / 180 * np.pi
        rotZ = [[np.cos(angle), -np.sin(angle), 0],
                [np.sin(angle), np.cos(angle), 0],
                [0, 0, 1]]
        
        return np.matmul(rotZ, self.points)
    
        

        
class Display():
    def __init__(self, width, height):
        pg.init()
        self.width, self.height = width, height
        self.screen = pg.display.set_mode([width, height])
        self.screen.fill((255, 255, 255))

        image = pg.image.load("01_icon.png")
        pg.display.set_icon(image)
        pg.display.set_caption("Cube")

        # Centre co-ordinates
        self.x, self.y  = self.width / 2, self.height / 2

        # 3D Matrix of all verticies in a cube
        self.length = self.width / 5 if self.width <= self.height else self.height / 5
        self.points = CubePoints(self.length)

    def draw_cube(self):
        self.screen.fill((255, 255, 255))

        # for i in range(4):
        #     pg.draw.line(
        #         self.screen,
        #         (100, 100, 100),
        #         (self.x + self.points.points[i][0], self.y + self.points.points[i][1]),
        #         (self.x + self.points.points[i + 4][0], self.y + self.points.points[i + 4][1]))
            
        for i in range(8):
            pg.draw.circle(self.screen, (150 + 0.25 * self.points.points[2][i], 100, 100), (self.x + self.points.points[0][i], self.y + self.points.points[1][i]), 4)
        self.points.points = self.points.rotateY(0.25)
        self.points.points = self.points.rotateZ(0.2)
        self.points.points = self.points.rotateX(0.1)

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
        #     if key == pg.K_RIGHT and screen.yPhase == 0: screen.yPhase = -90
        #     if key == pg.K_LEFT and screen.yPhase == 0: screen.yPhase = 90
        #     if key == pg.K_DOWN and screen.xPhase == 0: screen.xPhase = -90
        #     if key == pg.K_UP and screen.xPhase == 0: screen.xPhase = 90

        screen.draw_cube()
        pg.display.flip()
        pg.time.wait(5)
        
main()
pg.quit()