import pygame as pg
#from Display.display import Instance
from cube import Cube
from Pathfinding.cqueue import Queue
from Pathfinding.node import Node
from Pathfinding.binsearch import binSearch
from Pathfinding.mergesort import mergeSort

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
            return "UH OH"
        iter += 1

def main():     
    #cube = Cube(["WWWY",     "BGRG", "RGRW", "ORGO", "BWYY",      "YOBB"])
    cube = Cube()
    #cube.move(["U", "U", "R'", "U'", "F'", "U'", "R", "F", "F", "R'", "F", "F", "R'", "U"])
    cube.scramble()

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
    
main()