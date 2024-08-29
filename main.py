import threading
import pygame as pg
from numpy import pi

from Display.display import Display
from cube_2 import Cube_2
from cube_3 import Cube_3

from Assets.solve_2 import solve_2
from Assets.solve_3 import solve_3
from Assets.cqueue import Queue

MAX_FPS = 200
ROTATION_SPEED = 125
BG_SPEED = 40

WIDTH = 700
HEIGHT = 700

CUBE_TYPE = 3

SHIFT = (1, 2, 3)
MOVE_KEYS = {pg.K_u: "U",
             pg.K_r: "R",
             pg.K_f: "F",
             pg.K_d: "D",
             pg.K_l: "L",
             pg.K_b: "B",
             pg.K_m: "M",
             pg.K_s: "S",
             pg.K_e: "E",
             pg.K_LEFT: "Y",
             pg.K_RIGHT: "Y'",
             pg.K_UP: "X",
             pg.K_DOWN: "X'",
             pg.K_z: "Z"}

BUTTON_KEYS = {2: "U", 3: "U'",
               4: "F", 5: "F'",
               6: "R", 7: "R'",
               8: "D", 9: "D'",
               10: "B", 11: "B'",
               12: "L", 13: "L'"}

HALF_PI = pi / 2
DOUBLE_PI = pi * 2

BOB_SPEED = 500
BOB_STRENGTH = WIDTH * 0.02

class World:
    def __init__(self):
        pg.init()
        self.screen = Display(WIDTH, HEIGHT, BOB_STRENGTH, CUBE_TYPE)
        self.clock = pg.time.Clock()
        self.moveQueue = Queue(100)
        
    
               
    def findPath(self, cube):
        if CUBE_TYPE == 2:
            sNode, eNode = solve_2(cube)
        
        elif CUBE_TYPE == 3:
            sNode, eNode = solve_3(cube)

        path = []
        if sNode == None:
            return False
        while sNode.parent != None:
            path.append(sNode.movement)
            sNode = sNode.parent
        path = path[::-1]

        while eNode.parent != None:
            path.append(eNode.movement)
            eNode = eNode.parent

        return path
    
    def doEvents(self):
        for event in pg.event.get():
                if event.type == pg.QUIT: return False
                elif event.type == pg.KEYDOWN: self.keyDown, self.key = True, event.key
                elif event.type == pg.KEYUP: self.keyDown = False
                
        if self.keyDown == True:
            if self.key == pg.K_ESCAPE:
                return False
                                   
            else:
                if not self.screen.model.isMoving() and self.key in MOVE_KEYS.keys():
                    self.doMove(MOVE_KEYS[self.key], pg.key.get_mods())
                    
        # Get any buttons that are pressed
        pressed = self.screen.getPressed()
        if pressed != None and self.moveQueue.isEmpty() and not self.screen.model.isMoving():
            if not self.buttonDown:
                
                # Solve Button
                if pressed == 0:
                    solution = self.findPath(self.cube.cube)
                    if solution == False:
                        print("No solution")
                    elif solution == []:
                        print("Already Solved!")
                    else:
                        print(", ".join(solution))
                        for move in solution:
                            self.moveQueue.enqueue(move)
                    self.clock.tick()
                    
                # Scramble Button
                elif pressed == 1:
                    moves = self.cube.scramble()
                
                # Movement Buttons
                elif pressed in BUTTON_KEYS.keys():
                    self.doMove(BUTTON_KEYS[pressed], False)
                    
            self.buttonDown = True


        elif pressed == None:
            self.buttonDown = False
    
        return True
    
    def doMove(self, move, mod):
        if mod in SHIFT and move not in ("X", "X'", "Y", "Y'"): move += "'"
        self.cube.move(move)
        
        if move == "U": self.screen.model.uPhase = -HALF_PI
        elif move == "U'": self.screen.model.uPhase = HALF_PI
            
        elif move == "R": self.screen.model.rPhase = HALF_PI
        elif move == "R'": self.screen.model.rPhase = -HALF_PI
            
        elif move == "F": self.screen.model.fPhase = -HALF_PI
        elif move == "F'": self.screen.model.fPhase = HALF_PI
            
        elif move == "D": self.screen.model.dPhase = HALF_PI
        elif move == "D'": self.screen.model.dPhase = -HALF_PI
            
        elif move == "L": self.screen.model.lPhase = -HALF_PI
        elif move == "L'": self.screen.model.lPhase = HALF_PI
            
        elif move == "B": self.screen.model.bPhase = HALF_PI
        elif move == "B'": self.screen.model.bPhase = -HALF_PI
        
        elif move == "M": self.screen.model.mPhase = -HALF_PI
        elif move == "M'": self.screen.model.mPhase = HALF_PI
        
        elif move == "S": self.screen.model.sPhase = HALF_PI
        elif move == "S'": self.screen.model.sPhase = -HALF_PI
        
        elif move == "E": self.screen.model.ePhase = HALF_PI
        elif move == "E'": self.screen.model.ePhase = -HALF_PI
            
        elif move == "X": self.screen.model.xPhase = HALF_PI
        elif move == "X'": self.screen.model.xPhase = -HALF_PI
            
        elif move == "Y": self.screen.model.yPhase = -HALF_PI
        elif move == "Y'": self.screen.model.yPhase = HALF_PI
            
        elif move == "Z": self.screen.model.zPhase = -HALF_PI
        elif move == "Z'": self.screen.model.zPhase = HALF_PI

    def run(self):
        # Creating Cube object
        if CUBE_TYPE == 2:
            self.cube = Cube_2(["BROO", "RGGB", "WBWR", "YWYB", "GWYO", "OGYR"])

        elif CUBE_TYPE == 3:
            # self.cube = Cube_3(["GYYGWGWOY",    "OYGRRYWWO", "RGRRBGGOB", "GROWOYRBB", "BBWOGWYRB",    "YBWOYWOBR"])
            self.cube = Cube_3()

        # self.cube.scramble()

        iter = 0

        # World loop
        self.keyDown = False
        self.key = None
        self.buttonDown = False

        deltaTime = 0

        running = True
        self.clock.tick()
        while running:
            
            # Get and run input events (keys, buttons and others)
            running = self.doEvents()

            # Get moves from the movement queue
            if not self.moveQueue.isEmpty() and not self.screen.model.isMoving():
                move = self.moveQueue.dequeue()
                self.doMove(move, False)
            
            
            # Update aspects of the screen
            self.screen.model.phaseUpdate((deltaTime / ROTATION_SPEED) * HALF_PI)
            self.screen.cubeBob = (self.screen.cubeBob + deltaTime / BOB_SPEED) % DOUBLE_PI
            
            self.screen.backgroundPosition[0] = (self.screen.backgroundPosition[0] + deltaTime / BG_SPEED) % 90 - 90
            self.screen.backgroundPosition[1] = (self.screen.backgroundPosition[1] + deltaTime / BG_SPEED) % 90 - 90
            
            iter += 1
            if iter % MAX_FPS == 0:
                pg.display.set_caption(str(self.clock.get_fps()))
            
            # Draw the screen
            self.screen.drawScreen(self.cube.cube)

            deltaTime = self.clock.tick(MAX_FPS)
        pg.quit()

world = World()
world.run()