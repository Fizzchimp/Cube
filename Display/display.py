import pygame as pg
import numpy as np
from numpy import cos, sin, pi
from model import CubeModel

class Instance():
    def __init__(self, width, height):
        pg.init()

        # Setup the window
        self.width, self.height = width, height
        self.screen = pg.display.set_mode([width, height])
        self.screen.fill((255, 255, 255))
        image = pg.image.load("Display/01_icon.png")
        pg.display.set_icon(image)
        pg.display.set_caption("Cube")

        # Cube centre co-ordinates
        self.x, self.y  = self.width / 2, self.height / 2

        # 3D Matrix of all verticies in a cube
        length = self.width / 5 if self.width <= self.height else self.height / 5        
        self.newerPoints = CubeModel(length)
        
    

    def draw_cube(self):
        newerPoints = self.newerPoints.getPoints()
        for i in range(len(self.newerPoints.points)):
            for j in range(len(newerPoints[0][0])):
                newerPoints[i][0][j] += self.x
                newerPoints[i][1][j] += self.y

        self.screen.fill((255, 255, 255))

        for quad in newerPoints:
            if quad[2][0] < 0:
                shade = 125 + -0.5 * quad[2][0]
                pg.draw.polygon(self.screen, (shade, shade, shade), ((quad[0][0], quad[1][0]), 
                                                                    (quad[0][1], quad[1][1]),
                                                                    (quad[0][2], quad[1][2]),
                                                                    (quad[0][3], quad[1][3])))
                
                pg.draw.aalines(self.screen, (100, 100, 100), True, ((quad[0][0], quad[1][0]),
                                                                    (quad[0][1], quad[1][1]),
                                                                    (quad[0][2], quad[1][2]),
                                                                    (quad[0][3], quad[1][3])))


            if quad[2][4] < 0:
                shade = 125 + -0.5 * quad[2][4]
                pg.draw.polygon(self.screen, (shade, shade, shade), ((quad[0][4], quad[1][4]),
                                                                    (quad[0][1], quad[1][1]),
                                                                    (quad[0][2], quad[1][2]),
                                                                    (quad[0][5], quad[1][5])))
                
                pg.draw.aalines(self.screen, (100, 100, 100), True, ((quad[0][4], quad[1][4]),
                                                                    (quad[0][1], quad[1][1]),
                                                                    (quad[0][2], quad[1][2]),
                                                                    (quad[0][5], quad[1][5])))
                

            if quad[2][6] < 0:
                shade = 125 + -0.5 * quad[2][6]
                pg.draw.polygon(self.screen, (shade, shade, shade), ((quad[0][6], quad[1][6]),
                                                                    (quad[0][3], quad[1][3]),
                                                                    (quad[0][2], quad[1][2]),
                                                                    (quad[0][5], quad[1][5])))
                
                pg.draw.aalines(self.screen, (100, 100, 100), True, ((quad[0][6], quad[1][6]),
                                                                    (quad[0][3], quad[1][3]),
                                                                    (quad[0][2], quad[1][2]),
                                                                    (quad[0][5], quad[1][5])))
            
            #for i in range(len(quad[0])):
           #     pg.draw.circle(self.screen, (150 + -0.25 * quad[2][i], 100, 100), (quad[0][i], quad[1][i]), (self.width / 5 if self.width <= self.height else self.height / 5) / 25)
                

        if self.newerPoints.yPhase < 0: self.newerPoints.yPhase += 1
        if self.newerPoints.yPhase > 0: self.newerPoints.yPhase -= 1

        if self.newerPoints.xPhase < 0: self.newerPoints.xPhase += 1
        if self.newerPoints.xPhase > 0: self.newerPoints.xPhase -= 1

        if self.newerPoints.zPhase < 0: self.newerPoints.zPhase += 1
        if self.newerPoints.zPhase > 0: self.newerPoints.zPhase -= 1

        if self.newerPoints.uPhase < 0: self.newerPoints.uPhase += 1
        if self.newerPoints.uPhase > 0: self.newerPoints.uPhase -= 1

        if self.newerPoints.dPhase < 0: self.newerPoints.dPhase += 1
        if self.newerPoints.dPhase > 0: self.newerPoints.dPhase -= 1


def main():
    shiftKey = (1, 2)
    screen = Instance(700, 700)
    running = True
    keyDown = False
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT: running = False
            if event.type == pg.KEYDOWN: keyDown, key = True, event.key
            if event.type == pg.KEYUP: keyDown = False

        if keyDown:
            if key == pg.K_ESCAPE: running = False
            if not screen.newerPoints.isMoving():
                if key == pg.K_RIGHT: screen.newerPoints.yPhase += 90
                if key == pg.K_LEFT: screen.newerPoints.yPhase -= 90
                if key == pg.K_UP: screen.newerPoints.xPhase += 90
                if key == pg.K_DOWN: screen.newerPoints.xPhase -= 90
                if key == pg.K_z:
                    if pg.key.get_mods() in shiftKey: screen.newerPoints.zPhase += 90
                    else: screen.newerPoints.zPhase -= 90
                if key == pg.K_u:
                    if pg.key.get_mods() in shiftKey: screen.newerPoints.uPhase -= 90
                    else: screen.newerPoints.uPhase += 90
                if key == pg.K_d:
                    if pg.key.get_mods() in shiftKey: screen.newerPoints.dPhase -= 90
                    else: screen.newerPoints.dPhase += 90


        screen.draw_cube()
        pg.display.flip()
        pg.time.wait(4)
    pg.quit()
    
main()
