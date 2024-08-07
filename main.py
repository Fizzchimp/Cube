import threading
import pygame as pg
from numpy import pi
from Display.display import Display
from cube_2 import Cube_2
from cube_3 import Cube_3
from Assets.node_2 import Node
from Assets.cqueue import Queue
from Assets.binsearch import binSearch
from Assets.mergesort import mergeSort

MAX_FPS = 200
ROTATION_SPEED = 125
BG_SPEED = 40

WIDTH = 700
HEIGHT = 700

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
COL_KEYS = {"W":"YYYY", "G":"BBBB", "R":"OOOO", "B":"GGGG", "O":"RRRR", "Y":"WWWW"}
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
        self.screen = Display(WIDTH, HEIGHT, BOB_STRENGTH)
        self.clock = pg.time.Clock()
        self.moveQueue = Queue(100)
        
    def normalisedSolved(self, cube):
        # Returns a new solved state normalised to be comparable with start node
        return [
            COL_KEYS[cube[5][2]],
            
            cube[1][2] * 4,
            COL_KEYS[cube[4][3]],
            COL_KEYS[cube[1][2]],
            cube[4][3] * 4,

            cube[5][2] * 4
    ]

    def solve(self, startState):
        # Queue for the current nodes
        sNodeQ = Queue(99999)
        cSNode = Node(startState)

        eNodeQ = Queue(99999)
        cENode = Node(self.normalisedSolved(startState))

        generation = 0
        # List of visited nodes from the previous generation
        vENodes = []
        vSNodes = []
        
        while generation <= 6:
            # Start state tree
            vSNodes = []
            nextGen = generation + 1

            while cSNode.generation == generation:
                
                check, node = binSearch(vENodes, cSNode)
                if check == True:
                    return cSNode, node
                
                # Append current node to visited nodes
                vSNodes.append(cSNode)

                # Enqueue all adjacent nodes
                if cSNode.movement != "U'":  
                    sNodeQ.enqueue(Node(cSNode.U(), cSNode, "U", nextGen))
                if cSNode.movement != "U":   
                    sNodeQ.enqueue(Node(cSNode.U_Prime(), cSNode, "U'", nextGen))

                if cSNode.movement != "R'":  
                    sNodeQ.enqueue(Node(cSNode.R(), cSNode, "R", nextGen))
                if cSNode.movement != "R":   
                    sNodeQ.enqueue(Node(cSNode.R_Prime(), cSNode, "R'", nextGen))
                
                if cSNode.movement != "F'":  
                    sNodeQ.enqueue(Node(cSNode.F(), cSNode, "F", nextGen))
                if cSNode.movement != "F":   
                    sNodeQ.enqueue(Node(cSNode.F_Prime(), cSNode, "F'", nextGen))

                # Fetch the next node
                cSNode = sNodeQ.dequeue()

            # Sort visited nodes
            vSNodes = mergeSort(vSNodes)

            # End state tree
            vENodes = []
            while cENode.generation == generation:

                check, node = binSearch(vSNodes, cENode)
                if check == True:
                    return node, cENode

                # Append current node to visited nodes
                vENodes.append(cENode)

                # Enqueue all adjacent nodes
                if cENode.movement != "U'":
                    eNodeQ.enqueue(Node(cENode.U_Prime(), cENode, "U", nextGen))
                if cENode.movement != "U":   
                    eNodeQ.enqueue(Node(cENode.U(), cENode, "U'", nextGen))

                if cENode.movement != "R'":  
                    eNodeQ.enqueue(Node(cENode.R_Prime(), cENode, "R", nextGen))
                if cENode.movement != "R":   
                    eNodeQ.enqueue(Node(cENode.R(), cENode, "R'", nextGen))
                
                if cENode.movement != "F'":  
                    eNodeQ.enqueue(Node(cENode.F_Prime(), cENode, "F", nextGen))
                if cENode.movement != "F":   
                    eNodeQ.enqueue(Node(cENode.F(), cENode, "F'", nextGen))

                # Fetch the next node
                cENode = eNodeQ.dequeue()
                

            # Sort visited nodes
            vENodes = mergeSort(vENodes)

            # Increment the node generation counter
            generation += 1
            



        ### Final generation 7 check

        # Start tree
        vSNodes = []
        while True:
            try:
                check, node = binSearch(vENodes, cSNode)
                if check == True:
                    return cSNode, node
            
                # Append current node to visited nodes
                vSNodes.append(cSNode)
            
                # Fetch the next node
                cSNode = sNodeQ.dequeue()
                
            except:
                break
            
        # Sort visited nodes
        vSNodes = mergeSort(vSNodes)
        
        # End tree
        vENodes = []
        while True:
            try:
                check, node = binSearch(vSNodes, cENode)
                if check == True:
                    return node, cENode

                # Fetch the next node
                cENode = eNodeQ.dequeue()
                
            except:
                break
        return None, None
               
    def findPath(self, cube):
        sNode, eNode = self.solve(cube)
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
                    print(moves)
                
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
        #self.cube = Cube_2(["BROO", "RGGB", "WBWR", "YWYB", "GWYO", "OGYR"])
        # self.cube = Cube_3(["GYYGWGWOY",    "OYGRRYWWO", "RGRRBGGOB", "GROWOYRBB", "BBWOGWYRB",    "YBWOYWOBR"])
        self.cube = Cube_3()
        #gself.cube.scramble()

        iter = 0

        # World loop
        self.keyDown = False
        self.key = None
        self.buttonDown = False

        deltaTime = 0
        cubeBobbingPhase = 0

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