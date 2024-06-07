from re import S
import pygame as pg
from Display.model import CubeModel
colours = {"W": (245, 245, 245),
           "Y": (255, 255, 0),
           "G": (50, 205, 50),
           "R": (220, 20, 60),
           "B": (0, 0, 205),
           "O": (255, 140, 0)}

def depth(face):
    return face[4]

class Display():
    def __init__(self, width, height):
        pg.init()

        # Setup the window
        self.width, self.height = width, height
        self.screen = pg.display.set_mode([width, height])
        self.screen.fill((150, 150, 150))
        image = pg.image.load("Display/Textures/01_icon.png")
        pg.display.set_icon(image)
        pg.display.set_caption("Cube")

        # Cube centre co-ordinates
        self.x, self.y  = self.width / 2, self.height / 2

        # 3D Matrix of all verticies in a cube
        self.length = self.width / 5 if self.width <= self.height else self.height / 5        
        self.model = CubeModel(self.length)

        # Buttons
        self.button = Button((350, 600))
        
    

    def drawCube(self, cube):
        quadCol = [[colours[cube[0][0]], colours[cube[1][0]], colours[cube[4][1]]],
                   [colours[cube[0][1]], colours[cube[4][0]], colours[cube[3][1]]],
                   [colours[cube[0][2]], colours[cube[2][0]], colours[cube[1][1]]],
                   [colours[cube[0][3]], colours[cube[3][0]], colours[cube[2][1]]],

                   [colours[cube[5][0]], colours[cube[1][3]], colours[cube[2][2]]],
                   [colours[cube[5][1]], colours[cube[2][3]], colours[cube[3][2]]],
                   [colours[cube[5][2]], colours[cube[4][3]], colours[cube[1][2]]],
                   [colours[cube[5][3]], colours[cube[3][3]], colours[cube[4][2]]]]
        
        points = self.model.getPoints()
        faces = []
        
        for i, quad in enumerate(points):
            if quad[2][0] < 0:
                shade = 2 / 3 - quad[2][0] / self.length / 3
                faces.append(((quad[0][0] + self.x, quad[1][0] + self.y), 
                            (quad[0][1] + self.x, quad[1][1] + self.y),
                            (quad[0][2] + self.x, quad[1][2] + self.y),
                            (quad[0][3] + self.x, quad[1][3] + self.y),
                            (quad[2][0] + quad[2][1] + quad[2][2] + quad[2][3]) / 4,
                            (quadCol[i][0][0] * shade, quadCol[i][0][1] * shade, quadCol[i][0][2] * shade)))
                
            if quad[2][4] < 0:
                shade = 2 / 3 - quad[2][4] / self.length / 3
                faces.append(((quad[0][4] + self.x, quad[1][4] + self.y),
                            (quad[0][1] + self.x, quad[1][1] + self.y),
                            (quad[0][2] + self.x, quad[1][2] + self.y),
                            (quad[0][5] + self.x, quad[1][5] + self.y),
                            (quad[2][4] + quad[2][1] + quad[2][2] + quad[2][5]) / 4,
                            (quadCol[i][1][0] * shade, quadCol[i][1][1] * shade, quadCol[i][1][2] * shade)))
                
            if quad[2][6] < 0:   
                shade = 2 / 3 - quad[2][6] / self.length / 3
                faces.append(((quad[0][6] + self.x, quad[1][6] + self.y),
                            (quad[0][3] + self.x, quad[1][3] + self.y),
                            (quad[0][2] + self.x, quad[1][2] + self.y),
                            (quad[0][5] + self.x, quad[1][5] + self.y),
                            (quad[2][6] + quad[2][3] + quad[2][5] + quad[2][5]) / 4,
                            (quadCol[i][2][0] * shade, quadCol[i][2][1] * shade, quadCol[i][2][2] * shade)))
            
        for face in sorted(faces, key = depth, reverse = True):
            pg.draw.polygon(self.screen, face[5], face[0:4])
            pg.draw.aalines(self.screen, (50, 50, 50), True, face[0:4])

    def drawScreen(self, cube):
        self.screen.fill((150, 150, 150))
        self.drawCube(cube)

        mousePos = pg.mouse.get_pos()
        state = self.button.getState(mousePos)
        image, imagePos = self.button.getImage(state)
        self.screen.blit(image, imagePos)
        
        pg.display.flip()

    def getPressed(self):
        if self.button.getState(pg.mouse.get_pos()) == 2:
            return True
        return False

class Button():
    def __init__(self, centre):
        self.centre = centre
        self.width, self.height = 100, 50
        self.drawPointUp = (centre[0] - 54, centre[1] - 25)
        self.drawPointDown = (centre[0] - 50, centre[1] - 21)

        self.hitbox = ((self.centre[0] - 50, self.centre[1] - 25), (self.centre[0] + 50, self.centre[1] + 25))
        self.imageUp = pg.image.load("Display/Textures/Button_Up.png")
        self.imageHov = pg.image.load("Display/Textures/Button_Hovering.png")
        self.imageDown = pg.image.load("Display/Textures/Button_Down.png")

    def getImage(self, state):
        if state == 2: return self.imageDown, self.drawPointDown
        elif state == 1: return self.imageHov, self.drawPointUp
        else: return self.imageUp, self.drawPointUp
        
    def getState(self, mousePos):
        if self.hitbox[0][0] < mousePos[0] <self.hitbox[1][0] and self.hitbox[0][1] < mousePos[1] < self.hitbox[1][1]:
            if pg.mouse.get_pressed()[0]:
                return 2
            return 1
        return 0
     