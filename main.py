import pygame as pg
from Display.display import Instance
from cube import Cube
from Pathfinding.cqueue import Queue
from Pathfinding.node import Node
from Pathfinding.binsearch import binSearch
from Pathfinding.mergesort import mergeSort
SHIFT = (1, 2, 3)

class World:
    #def __init__(self):
    
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
    
    def run(self):
        iter = 0
        clock = pg.time.Clock()
        screen = Instance(700, 700)
        # cube = Cube(["RWGB",     "GGGG", "RRRR", "BBBB", "OOOO",      "YOBG"])
        cube = Cube()

        # World loop
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
                    if key == pg.K_RIGHT:
                        screen.model.yPhase += 90
                        cube.cube = cube.Y_Prime()

                    elif key == pg.K_LEFT:
                        screen.model.yPhase -= 90
                        cube.cube = cube.Y()

                    elif key == pg.K_UP:
                        screen.model.xPhase += 90
                        cube.cube = cube.X()

                    elif key == pg.K_DOWN:
                        screen.model.xPhase -= 90
                        cube.cube = cube.X_Prime()

                    elif key == pg.K_z:
                        if pg.key.get_mods() in SHIFT:
                            screen.model.zPhase += 90
                            cube.cube = cube.Z_Prime()
                        else:
                            screen.model.zPhase -= 90
                            cube.cube = cube.Z()

                    elif key == pg.K_u:
                        if pg.key.get_mods() in SHIFT:
                            screen.model.uPhase += 90
                            cube.cube = cube.U_Prime()
                        else:
                            screen.model.uPhase -= 90
                            cube.cube = cube.U()

                    elif key == pg.K_d:
                        if pg.key.get_mods() in SHIFT:
                            screen.model.dPhase -= 90
                            cube.cube = cube.D_Prime()
                        else:
                            screen.model.dPhase += 90
                            cube.cube = cube.D()

                    elif key == pg.K_f:
                        if pg.key.get_mods() in SHIFT:
                            screen.model.fPhase += 90
                            cube.cube = cube.F_Prime()
                        else:
                            screen.model.fPhase -= 90
                            cube.cube = cube.F()

                    elif key == pg.K_b:
                        if pg.key.get_mods() in SHIFT:
                            screen.model.bPhase -= 90
                            cube.cube = cube.B_Prime()
                        else:
                            screen.model.bPhase += 90
                            cube.cube = cube.B()

                    elif key == pg.K_l:
                        if pg.key.get_mods() in SHIFT:
                            screen.model.lPhase += 90
                            cube.cube = cube.L_Prime()
                        else:
                            screen.model.lPhase -= 90
                            cube.cube = cube.L()

                    elif key == pg.K_r:
                        if pg.key.get_mods() in SHIFT:
                            screen.model.rPhase -= 90
                            cube.cube = cube.R_Prime()
                        else:
                            screen.model.rPhase += 90
                            cube.cube = cube.R()
                    
                    elif key == pg.K_s:
                        print(", ".join(self.findPath(cube.cube)))


            iter += 1
            clock.tick()
            if iter % 100 == 0:
                print(clock.get_fps())


            screen.draw_cube(cube.cube)
            pg.display.flip()
            # pg.time.wait(8)
        pg.quit()
            


def repeat():
    world = World()
    cube = Cube()
    iter = 0
    while True:
        scramb = cube.scramble(20)
        path = world.findPath(cube.cube)
        if path != False:
            print(iter)
            if len(path) > 12:
                print(len(path), "moves:", scramb, ", ".join(path))
        else:
            print("UH OH")
            return
        iter += 1

def main():     
    cube = Cube(["BWBW",     "OOOO", "WGWG", "RRRR", "BYBY",      "GYGY"])
    # cube = Cube()
    # cube.move(["U", "U", "R'", "U'", "F'", "U'", "R", "F", "F", "R'", "F", "F", "R'", "U"])
    # cube.scramble()

    clock = pg.time.Clock()
    world = World()

    clock.tick()
    path = world.findPath(cube.cube)
    if path == False:
        print("Not solvable")
    else:
        print(", ".join(path))
    clock.tick()
    print(clock.get_time())
#main()

world = World()
world.run()