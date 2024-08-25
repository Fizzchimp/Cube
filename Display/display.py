import pygame as pg
from pygame import gfxdraw
from Display.model_2 import Model_2
from Display.model_3 import Model_3
from numpy import sin, cos, sqrt, arctan2

colours = {"W": (245, 245, 245),
           "Y": (255, 255, 0),
           "G": (50, 205, 50),
           "R": (220, 20, 60),
           "B": (0, 0, 205),
           "O": (255, 140, 0)}

BG_IMAGE_SIZE = 90

def depth(face):
    return face[4]

class Display():
    def __init__(self, width, height, bobStrength):

        # Setup the window
        self.width, self.height = width, height
        self.screen = pg.display.set_mode([width, height])
        image = pg.image.load("Display/Textures/01_icon.png")
        pg.display.set_icon(image)
        pg.display.set_caption("Cube")
    
        # Background
        image = pg.transform.scale(pg.image.load("Display/Textures/Background.png"), (BG_IMAGE_SIZE, BG_IMAGE_SIZE)).convert()
        dims = (BG_IMAGE_SIZE * (width // BG_IMAGE_SIZE + 2), BG_IMAGE_SIZE * (height // BG_IMAGE_SIZE + 2))
        self.dims = dims

        self.background = pg.Surface(dims)
        for i in range(dims[0] // BG_IMAGE_SIZE):
            for j in range(dims[1] // BG_IMAGE_SIZE):
                self.background.blit(image, (i * BG_IMAGE_SIZE, j * BG_IMAGE_SIZE))
        self.backgroundPosition = [-BG_IMAGE_SIZE, -BG_IMAGE_SIZE]

        ### Cube
        # Cube centre co-ordinates
        self.x, self.y  = 450, 300
        self.length = self.width / 5 if self.width <= self.height else self.height / 5

        self.cubeBob = 0
        self.bobStrength = bobStrength

        ### 2 by 2
        # 3D Matrix of all verticies in a cube
        self.cubeType = 2
        self.model = Model_2()
        
        ### 3 by 2
        # self.cubeType = 3
        # self.model = Model_3()

        # Buttons
        fontSize = 47
        startX, startY = 45, 30
        intervalX, intervalY = 80, 50
        gap = 10
        self.buttons = [Large_Button((250, 600), "SOLVE", 35),
                        Large_Button((450, 600), "SCRAMBLE", 35),
                        Button((startX, startY), "U", fontSize),
                        Button((startX + intervalX, startY), "U'", fontSize),
                        Button((startX, startY + intervalY), "F", fontSize),
                        Button((startX + intervalX, startY + intervalY), "F'", fontSize),
                        Button((startX, startY + intervalY * 2), "R", fontSize),
                        Button((startX + intervalX, startY + intervalY * 2), "R'", fontSize),
                        
                        Button((startX, startY + intervalY * 3 + gap), "D", fontSize),
                        Button((startX + intervalX, startY + intervalY * 3 + gap), "D'", fontSize),
                        Button((startX, startY + intervalY * 4 + gap), "B", fontSize),
                        Button((startX + intervalX, startY + intervalY * 4 + gap), "B'", fontSize),
                        Button((startX, startY + intervalY * 5 + gap), "L", fontSize),
                        Button((startX + intervalX, startY + intervalY * 5 + gap), "L'", fontSize)] 
        
    def drawLine(self, colour, p1, p2, width):
        centre = ((p1[0] + p2[0]) / 2,
                  (p1[1] + p2[1]) / 2)
        
        length = sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
        
        angle = arctan2(p2[0] - p1[0], p2[1] - p1[1])
        cosAngle = cos(angle)
        sinAngle = sin(angle)

        sinHaldWidth = (width / 2) * sinAngle
        cosHalfWidth = (width / 2) * cosAngle

        sinHalfLength = (length / 2) * sinAngle
        cosHalfLength = (length / 2) * cosAngle
        
        UL = (centre[0] + sinHalfLength - cosHalfWidth,
              centre[1] + cosHalfLength + sinHaldWidth)
        UR = (centre[0] - sinHalfLength - cosHalfWidth,
              centre[1] - cosHalfLength + sinHaldWidth)
        BL = (centre[0] + sinHalfLength + cosHalfWidth,
              centre[1] + cosHalfLength - sinHaldWidth)
        BR = (centre[0] - sinHalfLength + cosHalfWidth,
              centre[1] - cosHalfLength - sinHaldWidth)
        
        pg.gfxdraw.aapolygon(self.screen, (UL, UR, BR, BL), colour)
        pg.gfxdraw.filled_polygon(self.screen, (UL, UR, BR, BL), colour)

    def drawCube(self, cube, centreOffset = 0):
        x, y = self.x, self.y + centreOffset
        faces = []
        

        if self.cubeType == 2:
            quadCol = [[colours[cube[0][0]], colours[cube[1][0]], colours[cube[4][1]]],
                      [colours[cube[0][1]], colours[cube[4][0]], colours[cube[3][1]]],
                      [colours[cube[0][2]], colours[cube[2][0]], colours[cube[1][1]]],
                      [colours[cube[0][3]], colours[cube[3][0]], colours[cube[2][1]]],

                      [colours[cube[5][0]], colours[cube[1][3]], colours[cube[2][2]]],
                      [colours[cube[5][1]], colours[cube[2][3]], colours[cube[3][2]]],
                      [colours[cube[5][2]], colours[cube[4][3]], colours[cube[1][2]]],
                      [colours[cube[5][3]], colours[cube[3][3]], colours[cube[4][2]]]]
            
            points = self.model.getPoints()
            for i, quad in enumerate(points):
                if quad[2][0] < 0:
                    shade = (2 - quad[2][0]) / 3
                    faces.append(([quad[0][0] * self.length + x, quad[1][0] * self.length + y], 
                                [quad[0][1] * self.length + x, quad[1][1] * self.length + y],
                                [quad[0][2] * self.length + x, quad[1][2] * self.length + y],
                                [quad[0][3] * self.length + x, quad[1][3] * self.length + y],
                                (quad[2][0] + quad[2][1] + quad[2][2] + quad[2][3]) / 4,
                                (quadCol[i][0][0] * shade, quadCol[i][0][1] * shade, quadCol[i][0][2] * shade)))
                    

                if quad[2][4] < 0:
                    shade = (2 - quad[2][4]) / 3
                    faces.append(([quad[0][4] * self.length + x, quad[1][4] * self.length + y],
                                [quad[0][1] * self.length + x, quad[1][1] * self.length + y],
                                [quad[0][2] * self.length + x, quad[1][2] * self.length + y],
                                [quad[0][5] * self.length + x, quad[1][5] * self.length + y],
                                (quad[2][4] + quad[2][1] + quad[2][2] + quad[2][5]) / 4,
                                (quadCol[i][1][0] * shade, quadCol[i][1][1] * shade, quadCol[i][1][2] * shade)))
                    

                if quad[2][6] < 0:   
                    shade = (2 - quad[2][6]) / 3
                    faces.append(([quad[0][6] * self.length + x, quad[1][6] * self.length + y],
                                [quad[0][3] * self.length + x, quad[1][3] * self.length + y],
                                [quad[0][2] * self.length + x, quad[1][2] * self.length + y],
                                [quad[0][5] * self.length + x, quad[1][5] * self.length + y],
                                (quad[2][6] + quad[2][3] + quad[2][5] + quad[2][5]) / 4,
                                (quadCol[i][2][0] * shade, quadCol[i][2][1] * shade, quadCol[i][2][2] * shade)))

        if self.cubeType == 3:
            cornerCol = [(colours[cube[0][0]], colours[cube[1][0]], colours[cube[4][2]]),
                         (colours[cube[0][2]], colours[cube[4][0]], colours[cube[3][2]]),
                         (colours[cube[0][6]], colours[cube[2][0]], colours[cube[1][2]]),
                         (colours[cube[0][8]], colours[cube[3][0]], colours[cube[2][2]]),
                         
                         (colours[cube[5][6]], colours[cube[1][6]], colours[cube[4][8]]),
                         (colours[cube[5][8]], colours[cube[4][6]], colours[cube[3][8]]),
                         (colours[cube[5][0]], colours[cube[2][6]], colours[cube[1][8]]),
                         (colours[cube[5][2]], colours[cube[3][6]], colours[cube[2][8]])]
            
            sideCol = [(colours[cube[0][1]], colours[cube[4][1]]),
                       (colours[cube[0][3]], colours[cube[1][1]]),
                       (colours[cube[0][5]], colours[cube[3][1]]),
                       (colours[cube[0][7]], colours[cube[2][1]]),
                       
                       (colours[cube[1][3]], colours[cube[4][5]]),
                       (colours[cube[4][3]], colours[cube[3][5]]),
                       (colours[cube[2][3]], colours[cube[1][5]]),
                       (colours[cube[3][3]], colours[cube[2][5]]),
                       
                       (colours[cube[5][7]], colours[cube[4][7]]), 
                       (colours[cube[5][3]], colours[cube[1][7]]),
                       (colours[cube[5][5]], colours[cube[3][7]]),
                       (colours[cube[5][1]], colours[cube[2][7]])]
            
            centreCol = [colours[cube[0][4]],
                         colours[cube[1][4]],
                         colours[cube[2][4]],
                         colours[cube[3][4]],
                         colours[cube[4][4]],
                         colours[cube[5][4]]]
            

            corners, sides, centres = self.model.getPoints()
            
            for i, quad in enumerate(corners):
                if quad[2][-3] <= 0:
                    shade = (2 - quad[2][-3]) / 3
                    faces.append(([quad[0][0] * self.length + x, quad[1][0] * self.length + y], 
                                [quad[0][1] * self.length + x, quad[1][1] * self.length + y],
                                [quad[0][2] * self.length + x, quad[1][2] * self.length + y],
                                [quad[0][3] * self.length + x, quad[1][3] * self.length + y],
                                (quad[2][0] + quad[2][1] + quad[2][2] + quad[2][3]) / 4,
                                (cornerCol[i][0][0] * shade, cornerCol[i][0][1] * shade, cornerCol[i][0][2] * shade)))
                
                if quad[2][-2] <= 0:
                    shade = (2 - quad[2][-2]) / 3
                    faces.append(([quad[0][4] * self.length + x, quad[1][4] * self.length + y],
                                [quad[0][1] * self.length + x, quad[1][1] * self.length + y],
                                [quad[0][2] * self.length + x, quad[1][2] * self.length + y],
                                [quad[0][5] * self.length + x, quad[1][5] * self.length + y],
                                (quad[2][4] + quad[2][1] + quad[2][2] + quad[2][5]) / 4,
                                (cornerCol[i][1][0] * shade, cornerCol[i][1][1] * shade, cornerCol[i][1][2] * shade)))
                    
                if quad[2][-1] <= 0:
                    shade = (2 - quad[2][-1]) / 3
                    faces.append(([quad[0][6] * self.length + x, quad[1][6] * self.length + y],
                                [quad[0][3] * self.length + x, quad[1][3] * self.length + y],
                                [quad[0][2] * self.length + x, quad[1][2] * self.length + y],
                                [quad[0][5] * self.length + x, quad[1][5] * self.length + y],
                                (quad[2][6] + quad[2][3] + quad[2][5] + quad[2][5]) / 4,
                                (cornerCol[i][2][0] * shade, cornerCol[i][2][1] * shade, cornerCol[i][2][2] * shade)))
            
            for i, quad in enumerate(sides):
                if quad[2][-2] <= 0:
                    shade = (2 - quad[2][-2]) / 3
                    faces.append(([quad[0][0] * self.length + x, quad[1][0] * self.length + y],
                                  [quad[0][1] * self.length + x, quad[1][1] * self.length + y],
                                  [quad[0][2] * self.length + x, quad[1][2] * self.length + y],
                                  [quad[0][3] * self.length + x, quad[1][3] * self.length + y],
                                  [(quad[2][0] + quad[2][1] + quad[2][2] + quad[2][3]) / 4],
                                  (sideCol[i][0][0] * shade, sideCol[i][0][1] * shade, sideCol[i][0][2] * shade)))
                    
                if quad[2][-1] <= 0:
                    shade = (2 - quad[2][-1]) / 3
                    faces.append(([quad[0][1] * self.length + x, quad[1][1] * self.length + y],
                                  [quad[0][2] * self.length + x, quad[1][2] * self.length + y],
                                  [quad[0][5] * self.length + x, quad[1][5] * self.length + y],
                                  [quad[0][4] * self.length + x, quad[1][4] * self.length + y],
                                  [(quad[2][1] + quad[2][2] + quad[2][5] + quad[2][4]) / 4],
                                  (sideCol[i][1][0] * shade, sideCol[i][1][1] * shade, sideCol[i][1][2] * shade)))
                    
            for i, quad in enumerate(centres):
                if quad[2][-1] <= 0:
                    shade = (2 - quad[2][-1]) / 3
                    faces.append(([quad[0][0] * self.length + x, quad[1][0] * self.length + y],
                                  [quad[0][1] * self.length + x, quad[1][1] * self.length + y],
                                  [quad[0][2] * self.length + x, quad[1][2] * self.length + y],
                                  [quad[0][3] * self.length + x, quad[1][3] * self.length + y],
                                  (quad[2][0] + quad[2][1] + quad[2][2] + quad[2][3]) / 4,
                                  (centreCol[i][0] * shade, centreCol[i][1] * shade, centreCol[i][2] * shade)))

        for face in sorted(faces, key = depth, reverse = True):
            pg.gfxdraw.filled_polygon(self.screen, face[0:4], face[5])
                
            for i in range(4):
                self.drawLine((50, 50, 50), face[i], face[(i + 1) % 4], 8)
                pg.draw.circle(self.screen, (50, 50, 50), face[i], 4)
        
    def drawScreen(self, cube):
        # Draw the background of the screen
        self.screen.fill((200, 150, 100))
        #self.screen.blit(self.background, (self.backgroundPosition))
        
        # Draw the cube onto the screen
        self.drawCube(cube, self.bobStrength * sin(self.cubeBob))

        for button in self.buttons:
            image = button.getImage()
            self.screen.blit(image, button.drawPoint)
        
        pg.display.flip()
    
    def getPressed(self):
        mousePos = pg.mouse.get_pos()
        for i, button in enumerate(self.buttons):
            if button.getState(mousePos) == 2:
                return i

class Button():
    def __init__(self, centre, text, fontSize):
        # Images for the different button states
        self.imageUp = pg.image.load("Display/Textures/Button_Up.png").convert_alpha()
        self.imageHov = pg.image.load("Display/Textures/Button_Hov.png").convert_alpha()
        self.imageDown = pg.image.load("Display/Textures/Button_Down.png").convert_alpha()

        # Point where button is drawn
        self.drawPoint = (centre[0] - 39, centre[1] - 20)
        
        # Surface for text on the button
        font = pg.font.SysFont("Jhomuria", fontSize)
        textSurface = font.render(text, True, (0, 0, 0)).convert_alpha()
        dims = textSurface.get_size()
        textPoint = (39 - dims[0] / 2, 22 - dims[1] / 2)

        # Rendering the text on each button image
        self.imageUp.blit(textSurface, textPoint)
        self.imageHov.blit(textSurface, textPoint)
        self.imageDown.blit(textSurface, (textPoint[0], textPoint[1] + 4))

        # Hitbox for detecting mouse
        self.hitbox = ((centre[0] - 35, centre[1] - 20), (centre[0] + 35, centre[1] + 20))
        self.state = 0


    def getImage(self):
        if self.state == 2: return self.imageDown
        elif self.state == 1: return self.imageHov
        else: return self.imageUp
        
    def getState(self, mousePos):
        if self.hitbox[0][0] < mousePos[0] < self.hitbox[1][0] and self.hitbox[0][1] < mousePos[1] < self.hitbox[1][1]:
            if pg.mouse.get_pressed()[0]:
                self.state = 2
                return 2
            self.state = 1
            return 1
        self.state = 0
        return 0
     
class Large_Button():
    def __init__(self, centre, text, fontSize):
        # Images for the different button states
        self.imageUp = pg.image.load("Display/Textures/L_Button_Up.png").convert_alpha()
        self.imageHov = pg.image.load("Display/Textures/L_Button_Hov.png").convert_alpha()
        self.imageDown = pg.image.load("Display/Textures/L_Button_Down.png").convert_alpha()

        # Point where button is drawn
        self.drawPoint = (centre[0] - 79, centre[1] - 25)
        
        # Surface for text on the button
        font = pg.font.SysFont("Jhomuria", fontSize)
        textSurface = font.render(text, True, (0, 0, 0)).convert_alpha()
        dims = textSurface.get_size()
        textPoint = (79 - dims[0] / 2, 26 - dims[1] / 2)
        
        # Rendering the text on each button image
        self.imageUp.blit(textSurface, textPoint)
        self.imageHov.blit(textSurface, textPoint)
        self.imageDown.blit(textSurface, (textPoint[0], textPoint[1] + 4))

        # Hitbox for detecting mouse
        self.hitbox = ((centre[0] - 75, centre[1] - 25), (centre[0] + 75, centre[1] + 25))
        self.state = 0

    def getImage(self):
        if self.state == 2: return self.imageDown
        elif self.state == 1: return self.imageHov
        else: return self.imageUp

    def getState(self, mousePos):
        if self.hitbox[0][0] < mousePos[0] < self.hitbox[1][0] and self.hitbox[0][1] < mousePos[1] < self.hitbox[1][1]:
            if pg.mouse.get_pressed()[0]:
                self.state = 2
                return 2
            self.state = 1
            return 1
        self.state = 0
        return 0
    