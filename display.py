import pygame as pg
import numpy as np

alpha = 20 / 180 * np.pi
theta = 30 / 180 * np.pi
newAxis = [[np.cos(alpha), np.sin(theta) * np.sin(alpha), -np.cos(theta) * np.sin(alpha)],
        [0, np.cos(theta), np.sin(theta)],
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



class Display():
    def __init__(self, width, height):
        pg.init()
        self.width, self.height = width, height
        self.screen = pg.display.set_mode([width, height])
        self.screen.fill((255, 255, 255))

        image = pg.image.load("01_icon.png")
        pg.display.set_icon(image)
        pg.display.set_caption("Cube")

        # Cube centre co-ordinates
        self.x, self.y  = self.width / 2, self.height / 2

        # 3D Matrix of all verticies in a cube
        length = self.width / 5 if self.width <= self.height else self.height / 5
        self.cubePoints = [
            [length, length, -length, -length, length, length, -length, -length],
            [length, length, length, length, -length, -length, -length, -length],
            [length, -length, -length, length, length, -length, -length, length]]
        self.cubePoints = rotateX(theta * 180 / np.pi, rotateY(alpha * 180 / np.pi, self.cubePoints))

        self.yPhase = 0
        self.xPhase = 0
        self.zPhase = 0

    def draw_cube(self):
        points = rotateX(self.xPhase, (rotateY(self.yPhase, (rotateZ(self.zPhase, self.cubePoints)))))
        for i in range(8):
            points[0][i] += self.x
            points[1][i] += self.y


        self.screen.fill((255, 255, 255))
            
        for i in range(8):
            pg.draw.circle(self.screen, (150 + -0.25 * points[2][i], 100, 100), (points[0][i], points[1][i]), 4)

        for i in range(4):
            pg.draw.line(self.screen,
                         (100, 100, 100),
                         (points[0][i], points[1][i]),
                         (points[0][4 + i], points[1][i + 4]))
            
            pg.draw.line(self.screen,
                         (100, 100, 100),
                         (points[0][i], points[1][i]),
                         (points[0][(i + 1) % 4], points[1][(i + 1) % 4]))
            
            pg.draw.line(self.screen,
                         (100, 100, 100),
                         (points[0][i + 4], points[1][i + 4]),
                         (points[0][(i + 1) % 4 + 4], points[1][(i + 1) % 4 + 4]))
            
        shade1 = 150
        shade2 = 125
        shade3 = 100
        #pg.draw.polygon(self.screen,
        #                (shade1, shade1, shade1),
        #                ((points[0][0], points[1][0]),
        #                 (points[0][4], points[1][4]),
        #                 (points[0][5], points[1][5]),
        #                 (points[0][1], points[1][1])))
       # 
       # pg.draw.polygon(self.screen, 
       #                 (shade3, shade3, shade3),
       #                 ((points[0][2], points[1][2]),
       #                  (points[0][6], points[1][6]),
       #                  (points[0][7], points[1][7]),
       #                  (points[0][3], points[1][3])))
       # 
       # pg.draw.polygon(self.screen,
       #                 (shade2, shade2, shade2),
       #                 ((points[0][1], points[1][1]),
       #                  (points[0][5], points[1][5]),
       #                  (points[0][6], points[1][6]),
       #                  (points[0][2], points[1][2])))
       
        if self.yPhase < 0: self.yPhase += 1
        if self.yPhase > 0: self.yPhase -= 1

        if self.xPhase < 0: self.xPhase += 1
        if self.xPhase > 0: self.xPhase -= 1

        if self.zPhase < 0: self.zPhase += 1
        if self.zPhase > 0: self.zPhase -= 1

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
            if key == pg.K_SPACE: print(pg.key.get_pressed())
            if key == pg.K_RIGHT and screen.yPhase == 0: screen.yPhase += 90
            if key == pg.K_LEFT and screen.yPhase == 0: screen.yPhase -= 90
            if key == pg.K_UP and screen.xPhase == 0: screen.xPhase += 90
            if key == pg.K_DOWN and screen.xPhase == 0: screen.xPhase -= 90
            if key == pg.K_z and screen.zPhase == 0: screen.zPhase -= 90

        screen.draw_cube()
        pg.display.flip()
        pg.time.wait(5)
    pg.quit()
    
main()
