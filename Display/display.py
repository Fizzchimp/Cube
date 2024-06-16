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
        self.buttons = [Large_Button((250, 600), "SOLVE", 35),
                        Large_Button((450, 600), "SCRAMBLE", 35)
                        #Button((100, 100), "U", 50)
                        ]
        
        
    

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
                faces.append(([quad[0][0], quad[1][0]], 
                            [quad[0][1], quad[1][1]],
                            [quad[0][2], quad[1][2]],
                            [quad[0][3], quad[1][3]],
                            (quad[2][0] + quad[2][1] + quad[2][2] + quad[2][3]) / 4,
                            (quadCol[i][0][0] * shade, quadCol[i][0][1] * shade, quadCol[i][0][2] * shade)))
                
            if quad[2][4] < 0:
                shade = 2 / 3 - quad[2][4] / self.length / 3
                faces.append(([quad[0][4], quad[1][4]],
                            [quad[0][1], quad[1][1]],
                            [quad[0][2], quad[1][2]],
                            [quad[0][5], quad[1][5]],
                            (quad[2][4] + quad[2][1] + quad[2][2] + quad[2][5]) / 4,
                            (quadCol[i][1][0] * shade, quadCol[i][1][1] * shade, quadCol[i][1][2] * shade)))
                
            if quad[2][6] < 0:   
                shade = 2 / 3 - quad[2][6] / self.length / 3
                faces.append(([quad[0][6], quad[1][6]],
                            [quad[0][3], quad[1][3]],
                            [quad[0][2], quad[1][2]],
                            [quad[0][5], quad[1][5]],
                            (quad[2][6] + quad[2][3] + quad[2][5] + quad[2][5]) / 4,
                            (quadCol[i][2][0] * shade, quadCol[i][2][1] * shade, quadCol[i][2][2] * shade)))
            
        for face in sorted(faces, key = depth, reverse = True):
            for i in range(4):
                face[i][0] += self.x
                face[i][0] += self.y
            pg.draw.polygon(self.screen, face[5], face[0:4])
            pg.draw.aalines(self.screen, (50, 50, 50), True, face[0:4])

    def drawScreen(self, cube):
        self.screen.fill((150, 150, 150))
        self.drawCube(cube)

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
        self.imageUp = pg.image.load("Display/Textures/Button_Up.png")
        self.imageHov = pg.image.load("Display/Textures/Button_Hov.png")
        self.imageDown = pg.image.load("Display/Textures/Button_Down.png")

        # Point where button is drawn
        self.drawPoint = (centre[0] - 45, centre[1] - 25)
        
        # Surface for text on the button
        font = pg.font.SysFont("Jhomuria", fontSize)
        textSurface = font.render(text, True, (0, 0, 0))
        dims = textSurface.get_size()
        textPoint = (45 - dims[0] / 2, 26 - dims[1] / 2)

        # Rendering the text on each button image
        self.imageUp.blit(textSurface, textPoint)
        self.imageHov.blit(textSurface, textPoint)
        self.imageDown.blit(textSurface, (textPoint[0], textPoint[1] + 4))

        # Hitbox for detecting mouse
        self.hitbox = ((centre[0] - 50, centre[1] - 25), (centre[0] + 50, centre[1] + 25))
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
        self.imageUp = pg.image.load("Display/Textures/L_Button_Up.png")
        self.imageHov = pg.image.load("Display/Textures/L_Button_Hov.png")
        self.imageDown = pg.image.load("Display/Textures/L_Button_Down.png")

        # Point where button is drawn
        self.drawPoint = (centre[0] - 79, centre[1] - 25)
        
        # Surface for text on the button
        font = pg.font.SysFont("Jhomuria", fontSize)
        textSurface = font.render(text, True, (0, 0, 0))
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