import pygame as pg
from Display.display import Display
from cube import Cube
from Pathfinding.cqueue import Queue
from Pathfinding.node import Node
from Pathfinding.binsearch import binSearch
from Pathfinding.mergesort import mergeSort

SHIFT = (1, 2, 3)
MAX_FPS = 300
ROTATION_SPEED = 1000
WIDTH = 700
HEIGHT = 700

class World:
    def __init__(self):
        self.screen = Display(WIDTH, HEIGHT)
        self.clock = pg.time.Clock()
    def normalisedSolved(self, cube):
        # Returns a new solved state normalised to be comparable with start node
        colKeys = {"W":"YYYY", "G":"BBBB", "R":"OOOO", "B":"GGGG", "O":"RRRR", "Y":"WWWW"}
        return [
            colKeys[cube[5][2]],
            
            cube[1][2] * 4,
            colKeys[cube[4][3]],
            colKeys[cube[1][2]],
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
    
    def doKeyEvents(self, key):
            if key == pg.K_ESCAPE:
                return False
            if not self.screen.model.isMoving():
                if key == pg.K_RIGHT:
                    self.screen.model.yPhase += 90
                    self.cube.cube = self.cube.Y_Prime()

                elif key == pg.K_LEFT:
                    self.screen.model.yPhase -= 90
                    self.cube.cube = self.cube.Y()

                elif key == pg.K_UP:
                    self.screen.model.xPhase += 90
                    self.cube.cube = self.cube.X()

                elif key == pg.K_DOWN:
                    self.screen.model.xPhase -= 90
                    self.cube.cube = self.cube.X_Prime()

                elif key == pg.K_z:
                    if pg.key.get_mods() in SHIFT:
                        self.screen.model.zPhase += 90
                        self.cube.cube = self.cube.Z_Prime()
                    else:
                        self.screen.model.zPhase -= 90
                        self.cube.cube = self.cube.Z()

                elif key == pg.K_u:
                    if pg.key.get_mods() in SHIFT:
                        self.screen.model.uPhase += 90
                        self.cube.cube = self.cube.U_Prime()
                    else:
                        self.screen.model.uPhase -= 90
                        self.cube.cube = self.cube.U()

                elif key == pg.K_d:
                    if pg.key.get_mods() in SHIFT:
                        self.screen.model.dPhase -= 90
                        self.cube.cube = self.cube.D_Prime()
                    else:
                        self.screen.model.dPhase += 90
                        self.cube.cube = self.cube.D()

                elif key == pg.K_f:
                    if pg.key.get_mods() in SHIFT:
                        self.screen.model.fPhase += 90
                        self.cube.cube = self.cube.F_Prime()
                    else:
                        self.screen.model.fPhase -= 90
                        self.cube.cube = self.cube.F()

                elif key == pg.K_b:
                    if pg.key.get_mods() in SHIFT:
                        self.screen.model.bPhase -= 90
                        self.cube.cube = self.cube.B_Prime()
                    else:
                        self.screen.model.bPhase += 90
                        self.cube.cube = self.cube.B()

                elif key == pg.K_l:
                    if pg.key.get_mods() in SHIFT:
                        self.screen.model.lPhase += 90
                        self.cube.cube = self.cube.L_Prime()
                    else:
                        self.screen.model.lPhase -= 90
                        self.cube.cube = self.cube.L()

                elif key == pg.K_r:
                    if pg.key.get_mods() in SHIFT:
                        self.screen.model.rPhase -= 90
                        self.cube.cube = self.cube.R_Prime()
                    else:
                        self.screen.model.rPhase += 90
                        self.cube.cube = self.cube.R()
                    
                elif key == pg.K_s:
                    solution = self.findPath(self.cube.cube)
                    if solution == False:
                        print("No solution")
                    elif solution == []:
                        print("Already Solved!")
                    else:
                        print(", ".join(solution))
            return True
    
    def animateMoves(self, moves):
        for move in moves:
            print("A")

    def run(self):
        # Creating Cube object
        #self.cube = Cube(["WWWW", "GGGG",  "RRRR", "BBBB", "OOOO", "YYYY"])
        self.cube = Cube()

        iter = 0

        # World loop
        self.clock.tick()
        moveClock = pg.time.Clock()
        running = True
        keyDown = False
        moving = False
        while running:
            timeElapsed = 0
            for event in pg.event.get():
                if event.type == pg.QUIT: running = False
                if event.type == pg.KEYDOWN: keyDown, key = True, event.key
                if event.type == pg.KEYUP: keyDown = False
                
            if keyDown:
                running = self.doKeyEvents(key)


            self.screen.draw_cube(self.cube.cube)
            pg.display.flip()
            
            self.screen.model.phaseUpdate(2)

            iter += 1
            self.clock.tick(MAX_FPS)
            if iter % MAX_FPS == 0:
                pg.display.set_caption(str(self.clock.get_fps()))
            

        pg.quit()

world = World()
world.run()