import pygame as pg
from model import CubeModel
add = 0.5

def depth(face):
    return face[4]

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
        self.model = CubeModel(length)
        
    

    def draw_cube(self):
        points = self.model.getPoints()
        faces = []
        for quad in points:
            if quad[2][0] < 0:
                faces.append(((quad[0][0] + self.x, quad[1][0] + self.y), 
                            (quad[0][1] + self.x, quad[1][1] + self.y),
                            (quad[0][2] + self.x, quad[1][2] + self.y),
                            (quad[0][3] + self.x, quad[1][3] + self.y),
                            (quad[2][0] + quad[2][1] + quad[2][2] + quad[2][3]) / 4))
            if quad[2][4] < 0:    
                faces.append(((quad[0][4] + self.x, quad[1][4] + self.y),
                            (quad[0][1] + self.x, quad[1][1] + self.y),
                            (quad[0][2] + self.x, quad[1][2] + self.y),
                            (quad[0][5] + self.x, quad[1][5] + self.y),
                            (quad[2][4] + quad[2][1] + quad[2][2] + quad[2][5]) / 4))
            if quad[2][6] < 0:    
                faces.append(((quad[0][6] + self.x, quad[1][6] + self.y),
                            (quad[0][3] + self.x, quad[1][3] + self.y),
                            (quad[0][2] + self.x, quad[1][2] + self.y),
                            (quad[0][5] + self.x, quad[1][5] + self.y),
                            (quad[2][6] + quad[2][3] + quad[2][5] + quad[2][5]) / 4))
                
        # for i in range(len(points)):
        #     for j in range(len(points[0][0])):
        #         points[i][0][j] += self.x
        #         points[i][1][j] += self.y

        self.screen.fill((255, 255, 255))

        # for quad in points:
        #     if quad[2][0] < 0:
        #         shade = 125 + -0.5 * quad[2][0]
        #         pg.draw.polygon(self.screen, (shade, shade, shade), ((quad[0][0], quad[1][0]), 
        #                                                             (quad[0][1], quad[1][1]),
        #                                                             (quad[0][2], quad[1][2]),
        #                                                             (quad[0][3], quad[1][3])))
                
        #         pg.draw.aalines(self.screen, (100, 100, 100), True, ((quad[0][0], quad[1][0]),
        #                                                             (quad[0][1], quad[1][1]),
        #                                                             (quad[0][2], quad[1][2]),
        #                                                             (quad[0][3], quad[1][3])))


        #     if quad[2][4] < 0:
        #         shade = 125 + -0.5 * quad[2][4]
        #         pg.draw.polygon(self.screen, (shade, shade, shade), ((quad[0][4], quad[1][4]),
        #                                                             (quad[0][1], quad[1][1]),
        #                                                             (quad[0][2], quad[1][2]),
        #                                                             (quad[0][5], quad[1][5])))
                
        #         pg.draw.aalines(self.screen, (100, 100, 100), True, ((quad[0][4], quad[1][4]),
        #                                                             (quad[0][1], quad[1][1]),
        #                                                             (quad[0][2], quad[1][2]),
        #                                                             (quad[0][5], quad[1][5])))
                

        #     if quad[2][6] < 0:
        #         shade = 125 + -0.5 * quad[2][6]
        #         pg.draw.polygon(self.screen, (shade, shade, shade), ((quad[0][6], quad[1][6]),
        #                                                             (quad[0][3], quad[1][3]),
        #                                                             (quad[0][2], quad[1][2]),
        #                                                             (quad[0][5], quad[1][5])))
                
        #         pg.draw.aalines(self.screen, (100, 100, 100), True, ((quad[0][6], quad[1][6]),
        #                                                             (quad[0][3], quad[1][3]),
        #                                                             (quad[0][2], quad[1][2]),
        #                                                             (quad[0][5], quad[1][5])))
            
        for face in sorted(faces, key = depth, reverse = True):
            pg.draw.polygon(self.screen, (150, 150, 150), face[0:4])
            pg.draw.aalines(self.screen, (100, 100, 100), True, face[0:4])

        self.model.phaseUpdate(add)


def main():
    iter = 0
    clock = pg.time.Clock()
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
            if not screen.model.isMoving():
                if key == pg.K_RIGHT: screen.model.yPhase += 90
                elif key == pg.K_LEFT: screen.model.yPhase -= 90
                elif key == pg.K_UP: screen.model.xPhase += 90
                elif key == pg.K_DOWN: screen.model.xPhase -= 90
                elif key == pg.K_z:
                    if pg.key.get_mods() in shiftKey: screen.model.zPhase += 90
                    else: screen.model.zPhase -= 90
                elif key == pg.K_u:
                    if pg.key.get_mods() in shiftKey: screen.model.uPhase += 90
                    else: screen.model.uPhase -= 90
                elif key == pg.K_d:
                    if pg.key.get_mods() in shiftKey: screen.model.dPhase -= 90
                    else: screen.model.dPhase += 90
                elif key == pg.K_f:
                    if pg.key.get_mods() in shiftKey: screen.model.fPhase += 90
                    else: screen.model.fPhase -= 90
                elif key == pg.K_b:
                    if pg.key.get_mods() in shiftKey: screen.model.bPhase -= 90
                    else: screen.model.bPhase += 90
                elif key == pg.K_l:
                    if pg.key.get_mods() in shiftKey: screen.model.lPhase += 90
                    else: screen.model.lPhase -= 90
                elif key == pg.K_r:
                    if pg.key.get_mods() in shiftKey: screen.model.rPhase -= 90
                    else: screen.model.rPhase += 90

        iter += 1
        clock.tick()
        if iter % 100 == 0:
            print(clock.get_fps())


        screen.draw_cube()
        pg.display.flip()
        # pg.time.wait(8)
    pg.quit()
    
main()
