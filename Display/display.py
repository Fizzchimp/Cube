import pygame as pg
import numpy as np
from numpy import cos, sin
from model import CubeModel

alpha = 20 / 180 * np.pi
theta = 30 / 180 * np.pi
newAxis = [[np.cos(alpha), np.sin(theta) * np.sin(alpha), -np.cos(theta) * np.sin(alpha)],
        [0, cos(theta), np.sin(theta)],
        [np.sin(alpha), -np.sin(theta) * np.cos(alpha), np.cos(theta) * np.cos(alpha)]]

def rotateX(angle, points):
    angle = angle / 180 * np.pi
    axis = newAxis[0]
    rotX = [[np.cos(angle) + axis[0] * axis[0] * (1 - np.cos(angle)),
            axis[0] * axis[1] * (1 - np.cos(angle)) - axis[2] * np.sin(angle),
            axis[0] * axis[2] * (1 - np.cos(angle)) + axis[1] * np.sin(angle)],

            [axis[0] * axis[1] * (1 - np.cos(angle)) + axis[2] * np.sin(angle),
            np.cos(angle) + axis[1] * axis[1] * (1 - np.cos(angle)),
            axis[1] * axis[2] * (1 - np.cos(angle)) - axis[0] * np.sin(angle)],

            [axis[0] * axis[2] * (1 - np.cos(angle)) - axis[1] * np.sin(angle),
            axis[1] * axis[2] * (1 - np.cos(angle)) + axis[0] * np.sin(angle),
            np.cos(angle) + axis[2] * axis[2] * (1 - np.cos(angle))]]
        
    return np.matmul(rotX, points)

def rotateY(angle, points):
    angle = angle / 180 * np.pi
    axis = newAxis[1]
    rotY = [[np.cos(angle) + axis[0] * axis[0] * (1 - np.cos(angle)),
            axis[0] * axis[1] * (1 - np.cos(angle)) - axis[2] * np.sin(angle),
            axis[0] * axis[2] * (1 - np.cos(angle)) + axis[1] * np.sin(angle)],

            [axis[0] * axis[1] * (1 - np.cos(angle)) + axis[2] * np.sin(angle),
            np.cos(angle) + axis[1] * axis[1] * (1 - np.cos(angle)),
            axis[1] * axis[2] * (1 - np.cos(angle)) - axis[0] * np.sin(angle)],

            [axis[0] * axis[2] * (1 - np.cos(angle)) - axis[1] * np.sin(angle),
            axis[1] * axis[2] * (1 - np.cos(angle)) + axis[0] * np.sin(angle),
            np.cos(angle) + axis[2] * axis[2] * (1 - np.cos(angle))]]

    return np.matmul(rotY, points)

def rotateZ(angle, points):
    angle = angle / 180 * np.pi
    axis = newAxis[2]
    rotZ = [[np.cos(angle) + axis[0] * axis[0] * (1 - np.cos(angle)),
            axis[0] * axis[1] * (1 - np.cos(angle)) - axis[2] * np.sin(angle),
            axis[0] * axis[2] * (1 - np.cos(angle)) + axis[1] * np.sin(angle)],

            [axis[0] * axis[1] * (1 - np.cos(angle)) + axis[2] * np.sin(angle),
            np.cos(angle) + axis[1] * axis[1] * (1 - np.cos(angle)),
            axis[1] * axis[2] * (1 - np.cos(angle)) - axis[0] * np.sin(angle)],

            [axis[0] * axis[2] * (1 - np.cos(angle)) - axis[1] * np.sin(angle),
            axis[1] * axis[2] * (1 - np.cos(angle)) + axis[0] * np.sin(angle),
            np.cos(angle) + axis[2] * axis[2] * (1 - np.cos(angle))]]

    return np.matmul(rotZ, points)



class Instance():
    def __init__(self, width, height):
        pg.init()
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
        self.cubePoints = [
            [length,  length, -length, -length,  length,  length, -length, -length, length,      0,      0, -length,        0,       0],
            [length,  length,  length,  length, -length, -length, -length, -length,      0, length,      0,        0, -length,       0],
            [length, -length, -length,  length,  length, -length, -length,  length,      0,      0, length,        0,       0, -length]]
        
        
        self.newerPoints = CubeModel(length)
        
        self.cubePoints = rotateX(theta * 180 / np.pi, rotateY(alpha * 180 / np.pi, self.cubePoints))
        for i, quad in enumerate(self.newerPoints.points):
            self.newerPoints.points[i] = rotateX(theta * 180 / np.pi, rotateY(alpha * 180 / np.pi, quad))
        self.yPhase = 0
        self.xPhase = 0
        self.zPhase = 0


    def isMoving(self):
        # Check if animation is currently playing
        return True if self.xPhase != 0 or self.yPhase != 0 or self.zPhase != 0 else False
    

    def draw_cube(self):
        width = 1
        points = rotateX(self.xPhase, (rotateY(self.yPhase, (rotateZ(self.zPhase, self.cubePoints)))))
        for i in range(len(points[0])):
            points[0][i] += self.x
            points[1][i] += self.y


        newerPoints = []
        for i in range(len(self.newerPoints.points)):
            newerPoints.append(rotateX(self.xPhase, (rotateY(self.yPhase, (rotateZ(self.zPhase, self.newerPoints[i]))))))
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
                
                pg.draw.lines(self.screen, (100, 100, 100), True, ((quad[0][0], quad[1][0]),
                                                                    (quad[0][1], quad[1][1]),
                                                                    (quad[0][2], quad[1][2]),
                                                                    (quad[0][3], quad[1][3])), width)


            if quad[2][4] < 0:
                shade = 125 + -0.5 * quad[2][4]
                pg.draw.polygon(self.screen, (shade, shade, shade), ((quad[0][4], quad[1][4]),
                                                                    (quad[0][1], quad[1][1]),
                                                                    (quad[0][2], quad[1][2]),
                                                                    (quad[0][5], quad[1][5])))
                
                pg.draw.lines(self.screen, (100, 100, 100), True, ((quad[0][4], quad[1][4]),
                                                                    (quad[0][1], quad[1][1]),
                                                                    (quad[0][2], quad[1][2]),
                                                                    (quad[0][5], quad[1][5])), width)
                

            if quad[2][6] < 0:
                shade = 125 + -0.5 * quad[2][6]
                pg.draw.polygon(self.screen, (shade, shade, shade), ((quad[0][6], quad[1][6]),
                                                                    (quad[0][3], quad[1][3]),
                                                                    (quad[0][2], quad[1][2]),
                                                                    (quad[0][5], quad[1][5])))
                
                pg.draw.lines(self.screen, (100, 100, 100), True, ((quad[0][6], quad[1][6]),
                                                                    (quad[0][3], quad[1][3]),
                                                                    (quad[0][2], quad[1][2]),
                                                                    (quad[0][5], quad[1][5])), width)
            
            for i in range(len(quad[0])):
                pg.draw.circle(self.screen, (150 + -0.25 * quad[2][i], 100, 100), (quad[0][i], quad[1][i]), (self.width / 5 if self.width <= self.height else self.height / 5) / 25)
                

        # for i in range(4):
        #     pg.draw.aaline(self.screen,
        #                  (100, 100, 100),
        #                  (points[0][i], points[1][i]),
        #                  (points[0][4 + i], points[1][i + 4]))
            
        #     pg.draw.aaline(self.screen,
        #                  (100, 100, 100),
        #                  (points[0][i], points[1][i]),
        #                  (points[0][(i + 1) % 4], points[1][(i + 1) % 4]))
            
        #     pg.draw.aaline(self.screen,
        #                  (100, 100, 100),
        #                  (points[0][i + 4], points[1][i + 4]),
        #                  (points[0][(i + 1) % 4 + 4], points[1][(i + 1) % 4 + 4]))
            
       
        if self.yPhase < 0: self.yPhase += 1
        if self.yPhase > 0: self.yPhase -= 1

        if self.xPhase < 0: self.xPhase += 1
        if self.xPhase > 0: self.xPhase -= 1

        if self.zPhase < 0: self.zPhase += 1
        if self.zPhase > 0: self.zPhase -= 1

def main():
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
            if not screen.isMoving():
                if key == pg.K_RIGHT: screen.yPhase += 90
                if key == pg.K_LEFT: screen.yPhase -= 90
                if key == pg.K_UP: screen.xPhase += 90
                if key == pg.K_DOWN: screen.xPhase -= 90
                if key == pg.K_z: screen.zPhase -= 90

        screen.draw_cube()
        pg.display.flip()
        pg.time.wait(4)
    pg.quit()
    
main()
